import json
from pathlib import Path

from readmdict import MDD, MDX


XIANHAN_DIR = Path("D:/Documents/xianhan-7")
MDD_DIR = XIANHAN_DIR / "现汉7.mdd"
MDX_DIR = XIANHAN_DIR / "现汉7.mdx"
OUTPUT_DIR = XIANHAN_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class Xianhan:
    MDD_DATA: MDD
    MDX_DATA: MDX

    def __init__(self):
        self.MDD_DATA = MDD(MDD_DIR)
        self.MDX_DATA = MDX(MDX_DIR)

    def _sanitize_file_name(self, name: bytes) -> str:
        return name.decode("utf-8").replace("\\", "_")

    def save(self):
        for name, content in self.MDD_DATA.items():
            with open(OUTPUT_DIR / self._sanitize_file_name(name), "wb") as f:
                f.write(content)

        result = {}
        for name, content in self.MDX_DATA.items():
            result[name.decode("utf-8")] = content.decode("utf-8")

        with (OUTPUT_DIR / "result.json").open("w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)


xianhan = Xianhan()
xianhan.save()

output_str = (OUTPUT_DIR / "result.json").read_text(encoding="utf-8")
with (OUTPUT_DIR / "result.txt").open("w", encoding="utf-8") as f:
    f.write("\n".join(set(output_str)))
