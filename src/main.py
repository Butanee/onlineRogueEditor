# Authors https://github.com/JulianStiebler/
# Organization: https://github.com/rogueEdit/
# Repository: https://github.com/rogueEdit/OnlineRogueEditor
# Contributors: https://github.com/claudiunderthehood 
# Date of release: 13.06.2024
# Last Edited: 28.06.2024
# Based on: https://github.com/pagefaultgames/pokerogue/

"""
This script facilitates user login and session initialization for PokeRogue. It offers a menu-driven interface to 
perform various account and game data actions after a successful login using either requests or Selenium.

Features:
- User login through requests or Selenium.
- Various account and game data actions through a menu-driven interface.
- Custom logging and colored console output.

Modules:
- getpass: For securely obtaining the password from the user.
- requests: For handling HTTP sessions and requests.
- brotli: (Imported but not directly used in this script).
- loginLogic: Custom module for handling login logic using requests.
- Rogue: Custom module for initializing and interacting with the PokeRogue session.
- SeleniumLogic: Custom module for handling login using Selenium.
- cFormatter: Custom formatter for colored printing and logging.
- Color: Enumeration defining color codes for cFormatter.
- CustomLogger: Custom logging functionality.
- config: Custom module for configuration and update checking.
- datetime, timedelta: For date and time operations.
- colorama: For terminal text color formatting.
"""

import getpass
import requests
import brotli  # noqa: F401

from modules import requestsLogic, Rogue, SeleniumLogic, config
from modules.handler import OperationSuccessful, handle_operation_exceptions, OperationCancel, OperationSoftCancel
from colorama import Fore, Style, init
from utilities import cFormatter, Color, CustomLogger
from datetime import datetime, timedelta
from utilities import fh_printMessageBuffer
from sys import exit
from utilities import Generator
generator = Generator()
generator.generate()
init()
logger = CustomLogger()

if not config.debug:
    config.f_checkForUpdates(requests, datetime, timedelta, Style)


@handle_operation_exceptions
def m_executeOptions(choice_index, valid_choices):
    for idx, func in valid_choices:
        if idx == choice_index:
            func()
            break
        elif idx == 'exit':
            raise KeyboardInterrupt

@handle_operation_exceptions
def m_mainMenu(rogue, editOffline: bool = False):
    title = f'{config.title}>'
    useWhenDone = f'{Fore.LIGHTYELLOW_EX}(完成后使用)'
    reworked = f'{Fore.GREEN}(重构)'

    term = [
        (title, 'title'),
        ('账户操作', 'category'),
        ((f'{Fore.YELLOW}创建备份', reworked), rogue.f_createBackup),
        ((f'{Fore.YELLOW}恢复备份', reworked), rogue.f_restoreBackup),
        (('从服务器加载游戏数据', reworked), rogue.f_getGameData),
        (('编辑存档数据', reworked), rogue.f_changeSaveSlot),
        (('编辑帐户统计信息', reworked), rogue.f_editAccountStats),

        ('编辑', 'category'),
        ((f'{Fore.YELLOW}创建蛋', reworked), rogue.f_addEggsGenerator),
        ((f'编辑 {Fore.YELLOW}蛋孵化时间', reworked), rogue.f_editHatchWaves),
        ((f'编辑 {Fore.YELLOW}扭蛋券', reworked), rogue.f_addTicket),
        ((f'编辑 {Fore.YELLOW}一个初始宝可梦', reworked), rogue.f_editStarter),
        ((f'编辑 {Fore.YELLOW}某个初始宝可梦的{Style.RESET_ALL}糖果', reworked), rogue.f_addCandies),

        ('解锁', 'category'),
        ((f'解锁 {Fore.YELLOW}成就', reworked), rogue.f_unlockAchievements),
        ((f'解锁 {Fore.YELLOW}兑换券', reworked), rogue.f_unlockVouchers),
        ((f'解锁 {Fore.YELLOW}所有初始宝可梦', reworked), rogue.f_unlockStarters),
        ((f'解锁 {Fore.YELLOW}所有模式', reworked), rogue.f_unlockGamemodes),
        ((f'解锁 {Fore.YELLOW}所有', reworked), rogue.f_unlockAllCombined),

        ('会话数据操作', 'category'),
        ((f'Edit {Fore.YELLOW}当前的宝可梦派对', reworked), rogue.f_editPokemonParty),
        ((f'Edit {Fore.YELLOW}金额', reworked), rogue.f_editMoney),
        ((f'Edit {Fore.YELLOW}精灵球数量', reworked), rogue.f_editPokeballs),
        ((f'Edit {Fore.YELLOW}当前生物群落', reworked), rogue.f_editBiome),
        ((f'Edit {Fore.YELLOW}物品', reworked), rogue.f_submenuItemEditor),

        ('打印游戏信息', 'category'),
        (('显示所有宝可梦ID', reworked), rogue.legacy_pokedex),
        (('显示所有生物群落ID', reworked), rogue.legacy_printBiomes),
        (('显示所有招式ID', reworked), rogue.legacy_moves),
        (('显示所有兑换券ID', reworked), rogue.legacy_vouchers),
        (('显示所有性格ID', reworked), rogue.legacy_natures),
        (('显示所有性格槽ID', reworked), rogue.legacy_natureSlot),

        ('您也可以随时手动编辑 JSON！', 'helper'),
        ((f'{Fore.YELLOW}保存数据并上传到服务器', useWhenDone), rogue.f_updateAllToServer),
        (('打印帮助和程序信息', ''), config.f_printHelp),
        (('Logout', ''), rogue.f_logout),
        (title, 'title'),
    ]
    if editOffline or config.debug:
        # Filter entrys that would break offline
        term = [entry for entry in term if entry[1] != rogue.f_updateAllToServer]
        term = [entry for entry in term if entry[1] != rogue.f_getGameData]
        term = [entry for entry in term if entry[1] != rogue.f_logout]
        replacement_entry = ('直接应用离线编辑', 'helper')
        term = [replacement_entry if entry == ('您也可以随时手动编辑 JSON！', 'helper') else entry for entry in term]

    try:
        while True:
            validChoices = cFormatter.m_initializeMenu(term)
            fh_printMessageBuffer()
            userInput = input('命令:').strip().lower()

            if userInput == 'exit':
                raise KeyboardInterrupt
            if userInput.isdigit() and int(userInput) <= len(validChoices):
                choiceIndex = int(userInput)
                m_executeOptions(choiceIndex, validChoices)
            else:
                cFormatter.print(Color.INFO, '输入无效。请输入一个数字。')
    except OperationSuccessful as os:
        cFormatter.print(Color.DEBUG, f'操作成功：{os}')
    except KeyboardInterrupt:
        cFormatter.print(Color.DEBUG, '\n程序被用户中断。')
        exit()

@handle_operation_exceptions
def main():
    if config.debug:
        rogue = Rogue(requests.session(), auth_token="Invalid Auth Token", editOffline=config.debug)
        m_mainMenu(rogue)
    else:
        while True:
            try:
                config.f_printWelcomeText()
                loginChoice = int(input('请选择一种登录方式：'))
                if loginChoice not in [1, 2, 3, 4]:
                    cFormatter.print(Color.DEBUG, '请选择一个有效的选项。')
                    continue  # Prompt user again if choice is not valid

                if loginChoice != 4:
                    username = input('用户名: ')
                    password = getpass.getpass('密码（密码隐藏）：')


                session = requests.Session()
                if loginChoice == 1:
                    login = requestsLogic(username, password)
                    try:
                        if login.login():
                            cFormatter.print(Color.INFO, f'登录身份：{config.f_anonymizeName(username)}')
                            session.cookies.set('pokerogue_sessionId', login.sessionId, domain='pokerogue.net')
                            rogue = Rogue(session, login.token, login.sessionId)
                            break
                    except Exception as e:
                        cFormatter.print(Color.CRITICAL, f'出了点问题。{e}', isLogging=True)

                elif loginChoice in [2, 3]:
                    if loginChoice == 3:
                        cFormatter.print(Color.INFO, '不要关闭浏览器，不要操作游戏界面！')
                        cFormatter.print(Color.INFO, '不要关闭浏览器，不要操作游戏界面！')
                        cFormatter.print(Color.INFO, '不要关闭浏览器，不要操作游戏界面！')
                    seleniumLogic = SeleniumLogic(username, password, 120, useScripts=(loginChoice == 3))
                    sessionId, token, driver = seleniumLogic.logic()

                    if sessionId and token:
                        if not driver:
                            driver = None
                            print('Driver error')
                        cFormatter.print(Color.INFO, f'登录身份：{config.f_anonymizeName(username)}')
                        session.cookies.set('pokerogue_sessionId', sessionId, domain='pokerogue.net')
                        rogue = Rogue(session, auth_token=token, clientSessionId=sessionId, driver=driver, useScripts=(loginChoice == 3))
                        break
                    else:
                        cFormatter.print(Color.CRITICAL, '无法从 Selenium 检索必要的身份验证数据。')


                elif loginChoice == 4:
                    rogue = Rogue(session, auth_token='Invalid Auth Token', editOffline=True)
                    break

                else:
                    cFormatter.print(Color.CRITICAL, '无效的选择。请选择有效的方法。')

            except KeyboardInterrupt:
                exit()
        m_mainMenu(rogue, editOffline=(loginChoice == 4))

if __name__ == '__main__':
    while True:
        try:
            main()
        except OperationSuccessful as os:
            cFormatter.print(Color.DEBUG, f'操作成功：{os}')
        except KeyboardInterrupt:
            cFormatter.print(Color.DEBUG, '\n程序被用户中断。')
            exit()
        except OperationCancel:
            cFormatter.print(Color.DEBUG, '\n程序被用户中断.')
            exit()
        except OperationSoftCancel:
            cFormatter.print(Color.DEBUG, '\n程序被用户中断.')
            exit()

    
