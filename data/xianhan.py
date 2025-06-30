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


def save_xianhan():
    XIANHAN_DIR = Path("D:/Documents/xianhan-7")
    MDD_DIR = XIANHAN_DIR / "现汉7.mdd"
    MDX_DIR = XIANHAN_DIR / "现汉7.mdx"
    OUTPUT_DIR = XIANHAN_DIR / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    xianhan = Dictionary(MDD_DIR, MDX_DIR)
    xianhan.save(OUTPUT_DIR)

    output_str = (OUTPUT_DIR / "result.json").read_text(encoding="utf-8")
    with (OUTPUT_DIR / "result.txt").open("w", encoding="utf-8") as f:
        f.write("\n".join(set(output_str)))


def save_xinhua():
    XINHUA_DIR = Path("D:/Documents/xinhua-12")
    MDD_DIR = XINHUA_DIR / "新华字典12版图声.mdd"
    MDX_DIR = XINHUA_DIR / "新华字典12版图声.mdx"
    OUTPUT_DIR = XINHUA_DIR / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    xinhua = Dictionary(MDD_DIR, MDX_DIR)
    xinhua.save(OUTPUT_DIR)

    output_str = (OUTPUT_DIR / "result.json").read_text(encoding="utf-8")
    with (OUTPUT_DIR / "result.txt").open("w", encoding="utf-8") as f:
        f.write("\n".join(set(output_str)))


if __name__ == "__main__":
    save_xinhua()
