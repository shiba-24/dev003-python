import click
import importlib.util
import sys
from pathlib import Path

def hoge():
    return "pre-processing"

def load_module(input_module_path: Path):
    spec = importlib.util.spec_from_file_location(input_module_path.stem, input_module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[input_module_path.stem] = module
    spec.loader.exec_module(module)
    return module

@click.command()
@click.option("--input-module-path", type=click.Path(exists=True, path_type=Path), required=True)
def main(input_module_path):

    # 前処理（共通）
    fuga = hoge()

    # 本処理（可変にしたい）
    runner = load_module(input_module_path)
    runner.run()

if __name__ == "__main__":
    main()
