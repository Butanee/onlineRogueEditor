# Authors https://github.com/JulianStiebler/
# Organization: https://github.com/rogueEdit/
# Repository: https://github.com/rogueEdit/OnlineRogueEditor
# Contributors: None except Authors
# Date of release: 06.06.2024 
# Last Edited: 28.06.2024

"""
Online Rogue Editor Update Checker and Initialization

This script checks for updates on a GitHub repository and initializes necessary directories
for logging and backups if they do not already exist.

Modules:
- requests: HTTP library for sending GET and POST requests to GitHub's API.
- datetime: Provides classes for manipulating dates and times.
- timedelta: Represents a duration, the difference between two dates or times.
- utilities.cFormatter: Custom formatter for printing colored console output.
- os: Provides functions for interacting with the operating system, such as creating directories.

Workflow:
1. Initialize necessary directories (logs, backups, data) if they do not exist.
2. Check for updates on the GitHub repository using `check_for_updates` function.
3. Print initialization messages and helpful information using `initialize_text` and `print_help` functions.
"""

import os
from datetime import datetime, timedelta
import requests
# need to manually do it to avoid circular imports
from colorama import Fore, Style, init

init(autoreset=True)

logsDirectory: str = os.path.join(os.getcwd(), 'logs')
backupDirectory: str = os.path.join(os.getcwd(), 'backups')
dataDirectory: str = os.path.join(os.getcwd(), 'data')
timestampFile: str = os.path.join(dataDirectory, 'extra.json')

if not os.path.exists(logsDirectory):
    os.makedirs(logsDirectory)
    print(f'{Fore.GREEN}创建日志目录：{logsDirectory}')
# Create the backups directory if it doesn't exist
if not os.path.exists(backupDirectory):
    os.makedirs(backupDirectory)
    print(f'{Fore.GREEN}创建备份目录：{backupDirectory}')
if not os.path.exists(dataDirectory):
    os.makedirs(dataDirectory)
    print(f'{Fore.GREEN}创建的数据目录：{dataDirectory}')


# Settings this to true will deactivate backups, skip prompts and use offline mode automatically
debug: bool = False
debugDeactivateBackup: bool = True if debug else False
debugEnableTraceback: bool = True if debug else False

cacertURL = 'https://curl.se/ca/cacert.pem'
cacertPath = f'{dataDirectory}/cacert.pem'
if not os.path.exists(cacertPath):
    print(f'{Fore.RED}\ncacert.pem 未找到。SSL 连接需要此文件。\从{cacertURL}获取...{Style.RESET_ALL}。')
    print(f'{Fore.RED}\n如果是第一次启动，这很正常。')
    # Fetch the file using requests library
    response = requests.get(cacertURL)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to local file
        with open(cacertPath, 'wb') as f:
            f.write(response.content)
        print(f'{Fore.GREEN}成功获取 {cacertURL} 并保存为 {cacertPath}.{Style.RESET_ALL}.')
    else:
        print(f'获取 {cacertURL} 失败。\状态代码： {response.status_code}. \n 无法使用 SSL，但程序可能可以工作。')
        cacertPath = False

useCaCert = False if debug else cacertPath
version: str = 'v0.4'
title: str = f'<(^.^(< pyRogue {version} >)^.^)>'
owner: str = 'rogueEdit'
repo: str = 'onlineRogueEditor'
repoURL: str = f'https://github.com/{owner}/{repo}/'
releaseDate: str = '28.06.2024 3:59' # releaed 1:30 roughly but setting ahead in case some stuff pops up


def f_checkForUpdates(requests: requests, datetime: datetime, timedelta: timedelta, Style: object) -> None:
    """
    Check for updates on the GitHub repository since a specified release date.

    Args:
        requests (requests): HTTP library for sending requests to GitHub's API.
        datetime (datetime): Module for date and time manipulation.
        timedelta (timedelta): Represents a duration, the difference between two dates or times.
        Style (object): Object representing a formatting style (not used in this function).

    Usage Example:
        >>> check_for_updates(requests, datetime, timedelta, Style)

    Output Example:
        - Prints commit details if updates are found.
        - Provides a URL to view the latest code.
        - Advises updating the source code if updates are found.

    Modules/Librarys used and for what purpose exactly in each function:
    - requests: Sends HTTP GET requests to retrieve commit history from GitHub repository.
    - datetime: Converts release date to ISO 8601 format for GitHub API query.
    - timedelta: Calculates local timezone offset for converting release date to UTC.
    - utilities.cFormatter: Prints colored console output for displaying update details.
    """
    def f_convertToISOFormat(date_string: str, timedelta: timedelta) -> str:
        """
        Convert a date string to ISO 8601 format in UTC timezone.

        Args:
            date_string (str): Date string in format 'dd.mm.yyyy HH:MM'.
            timedelta (timedelta): Represents a duration, the difference between two dates or times.

        Returns:
            str: ISO 8601 formatted date string in UTC timezone.

        Raises:
            ValueError: If the input date format is incorrect.

        Usage Example:
            >>> convert_to_iso_format('20.06.2024 6:00', timedelta)

        Modules/Librarys used and for what purpose exactly in each function:
        - datetime: Parses and formats the input date string.
        """
        # Parse the input date string
        dateFormat = '%d.%m.%Y %H:%M'
        try:
            dt = datetime.strptime(date_string, dateFormat)
        except ValueError as e:
            raise ValueError("日期格式不正确，应为“dd.mm.yyyy HH：MM”") from e

        # Determine local timezone offset for Central European Time (CET)
        isDST = datetime.now().timetuple().tm_isdst
        timezoneOffset = timedelta(hours=2) if isDST else timedelta(hours=1)

        # Apply local timezone offset to convert to UTC
        utcDT = dt - timezoneOffset

        # Format datetime object to ISO 8601 format with UTC timezone 'Z' (Zulu time)
        isoFormat = utcDT.strftime('%Y-%m-%dT%H:%M:%SZ')

        return isoFormat

    try:
        # Convert release date to ISO 8601 format
        check_date = datetime.fromisoformat(f_convertToISOFormat(releaseDate, timedelta))

        # Construct GitHub API URL and parameters
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        params = {'since': check_date.isoformat()}

        # Send GET request to GitHub API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        commits = response.json()  # Parse JSON response

        # Extract commit titles and SHAs
        commitList = [{'sha': commit['sha'], 'message': commit['commit']['message']} for commit in commits]

        if commitList:
            print(f'{Fore.YELLOW}********* 发现过期源代码。新提交： *********{Style.RESET_ALL}')
            for commit in commitList:
                print(f'{Fore.YELLOW}---- 提交名称：({commit["message"]}{Style.RESET_ALL})')
                print(f'{Fore.BLUE}------> with SHA ({commit["sha"]}{Style.RESET_ALL})')
            print(f'{Fore.YELLOW}您可以在此处查看最新代码：{repoURL}{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}强烈建议更新源代码。有些事情可能无法按预期工作。{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}------------------------------------------------------------{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}未找到更新。')

    except ValueError as ve:
        print(f'{Fore.RED}无法解决 check_for_updates（） - 发生 ValueError：{ve}')
    except requests.exceptions.RequestException as re:
        print(f'{Fore.RED}无法解决 check_for_updates（） - 发生 RequestException：{re}')
    except Exception as e:
        print(f'{Fore.RED}无法解决 check_for_updates（） - 发生意外错误：{e}')

def f_printWelcomeText() -> None:
    """
    Print initialization messages for the program.

    This function prints messages regarding program initialization, network settings, and program version.

    Usage Example:
        >>> initialize_text()

    Modules/Librarys used and for what purpose exactly in each function:
    - utilities.cFormatter: Prints colored console output for initialization messages.
    """
    print(f'{Fore.GREEN}<pyRogue {version}>')
    print(f'{Fore.GREEN}我们会在每次登录时创建基本备份，并在您每次手动启动或选择时创建进一步的备份。')
    print(f'{Fore.GREEN}如有问题，请切换您的网络（热点、VPN 等）。')
    print(f'{Fore.GREEN}否则，请访问 {repoURL} 并报告问题。')
    print('------------------------------------------------------------')
    print(f'{Fore.MAGENTA}{Style.BRIGHT}1: 直接登录    可靠性 6/10')
    print(f'{Fore.MAGENTA}{Style.BRIGHT}2: 使用本地浏览器。   可靠性 7/10')
    print(f'{Fore.MAGENTA}{Style.BRIGHT}3: 使用本地浏览器和JS  可靠性 9/10')
    print(f'{Fore.MAGENTA}{Style.BRIGHT}4: 离线编辑trainer.json')

def f_printHelp() -> None:
    """
    Print helpful information for the user.

    This function prints various helpful messages for the user, including information
    about manual JSON editing, assistance through the program's GitHub page, release
    version details, and cautions about account safety and program authenticity.

    Usage Example:
        >>> print_help()

    Modules/Librarys used and for what purpose exactly in each function:
    - utilities.cFormatter: Prints colored console output for help messages.
    """
    print(f'{Fore.YELLOW}您也可以随时手动编辑 JSON。')
    print(f'{Fore.YELLOW}如果您需要帮助，请参阅该计划的 GitHub 页面。')
    print(f'{Fore.YELLOW}{repoURL}')
    print(f'{Fore.YELLOW}发布版本为:{version}- 请将其包含在您的问题或问题报告中。')
    print(f'{Fore.YELLOW}此版本现在还具有日志文件。')
    print(f'{Fore.YELLOW}如果您的帐户被标记或禁止，我们概不负责，并且')
    print(f'{Fore.YELLOW}你永远不知道这个程序是否有克隆。如果您不确定，')
    print(f'{Fore.YELLOW}请计算此二进制文件的校验和并访问{repoURL}')
    print(f'{Fore.YELLOW}要查看它应该具有的值，请从源代码中知道它的原始值。')

def f_anonymizeName(username):
    if len(username) < 3:  # If username length is less than 3, return as is (minimum 2 characters)
        return username
    
    visibleChars = max(int(len(username) * 0.2), 1)  # Calculate how many characters to leave visible
    startVisible = max(visibleChars // 2, 1)  # At least 1 character visible from the start
    endVisible = visibleChars - startVisible  # Remaining visible characters from the end
    
    # Construct the masked username
    maskedUsername = username[:startVisible] + '*' * (len(username) - startVisible - endVisible)
    
    return maskedUsername
    