import json
from pathlib import Path

from readmdict import MDD, MDX


class Dictionary:
    MDD_DATA: MDD
    MDX_DATA: MDX

    def __init__(self, mdd_dir: Path, mdx_dir: Path):
        self.MDD_DATA = MDD(mdd_dir)
        self.MDX_DATA = MDX(mdx_dir)

    def _sanitize_file_name(self, name: bytes) -> str:
        return name.decode("utf-8").replace("\\", "_")

    def save(self, output_dir: Path):
        for name, content in self.MDD_DATA.items():
            with open(output_dir / self._sanitize_file_name(name), "wb") as f:
                f.write(content)

        result = {}
        for name, content in self.MDX_DATA.items():
            result[name.decode("utf-8")] = content.decode("utf-8")

        with (output_dir / "result.json").open("w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)


def build(dict_dir: Path, name_stem: str):
    MDD_DIR = dict_dir / f"{name_stem}.mdd"
    MDX_DIR = dict_dir / f"{name_stem}.mdx"
    OUTPUT_DIR = dict_dir / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dictionary = Dictionary(MDD_DIR, MDX_DIR)
    dictionary.save(OUTPUT_DIR)

    output_str = (OUTPUT_DIR / "result.json").read_text(encoding="utf-8")
    with (OUTPUT_DIR / "result.txt").open("w", encoding="utf-8") as f:
        f.write("\n".join(set(output_str)))


build(Path("D:/Documents/xianhan-7"), "现汉7")
build(Path("D:/Documents/xinhua-12"), "新华字典12版图声")
build(Path("D:/Documents/guhan-2"), "古代汉语词典2 (2014)")
