import os
import json

def f_parseJSON(input_filepath: str, output_directory: str) -> None:
    """
    Parses a JSON file and generates a Python file with a class definition.

    Args:
    - input_filepath (str): Path to the input JSON file.
    - output_directory (str): Directory where the generated Python file should be saved.
    """
    try:
        with open(input_filepath, 'r') as infile:
            data = json.load(infile)

        # Determine the output filename based on the input filename
        filename = os.path.splitext(os.path.basename(input_filepath))[0]
        className = filename.title() + "Enum"
        output_filepath = os.path.join(output_directory, f"{filename.lower()}.py")

        # Generate the Python script content
        scriptContent = f"# 从枚举导入枚举\n\n"
        scriptContent += f"class {className}(Enum):\n"
        scriptContent += f"    {className}_DICT = {{\n"

        # Format each entry with new line and indentation
        for key, inner_dict in data.items():
            scriptContent += f"        '{key}': {{\n"
            for subkey, value in inner_dict.items():
                scriptContent += f"            '{subkey}': {value},\n"
            scriptContent += f"        }},\n"

        scriptContent += f"    }}\n"

        # Write the script content to a Python file
        with open(output_filepath, 'w') as outfile:
            outfile.write(scriptContent)

        print(f"为'{className}'生成的 Python 文件保存到'{output_filepath}'中.")

    except FileNotFoundError:
        print(f"错误:文件'{input_filepath}'没找到")
    except json.JSONDecodeError:
        print(f"错误：无法从JSON{input_filepath}解码 '.")
    except Exception as e:
        print(f"错误:{e}")

def f_processJSON(inputDir: str, outputDir: str) -> None:
    """
    Processes all JSON files in the given directory and converts them to Python files with class definitions.

    Args:
    - input_directory (str): Directory containing JSON files to process.
    - output_directory (str): Directory where the generated Python files should be saved.
    """
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)

        # Iterate over all JSON files in the input directory
        for filename in os.listdir(inputDir):
            if filename.endswith(".json"):
                inputFilepath = os.path.join(inputDir, filename)

                # Parse JSON file and generate Python file
                f_parseJSON(inputFilepath, outputDir)

    except Exception as e:
        print(f"处理 JSON 文件时出错：{e}")

# Example usage:
inputDir = '../../data'
outputDir = './converted'

f_processJSON(inputDir, outputDir)
