import click
from pathlib import Path

import processing

def hoge():
    return "pre-processing"

@click.command()
@click.option("--input-module-name", type=click.STRING, required=True)
def main(input_module_name):

    # 前処理（共通）
    fuga = hoge()

    # 本処理（可変にしたい）
    if input_module_name == "say_hello":
        runner = processing.say_hello
    elif input_module_name == "say_whatsup":
        runner = processing.say_whatsup
    runner.run()

if __name__ == "__main__":
    main()
