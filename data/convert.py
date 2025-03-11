import re


md_dir = "article/006_script_block_translation.md"
md2_dir = "article/007_roadmap_translation.md"
txt_dir = "data/Blocks.txt"

start = """# Format:
# Start Code..End Code; Block Name

# ================================================

# Note:   When comparing block names, casing, whitespace, hyphens,
#         and underbars are ignored.
#         For example, "Latin Extended-A" and "latin extended a" are equivalent.
#         For more information on the comparison of property values,
#            see UAX #44: http://www.unicode.org/reports/tr44/
#
#  All block ranges start with a value where (cp MOD 16) = 0,
#  and end with a value where (cp MOD 16) = 15. In other words,
#  the last hexadecimal digit of the start of range is ...0
#  and the last hexadecimal digit of the end of range is ...F.
#  This constraint on block ranges guarantees that allocations
#  are done in terms of whole columns, and that code chart display
#  never involves splitting columns in the charts.
#
#  All code points not explicitly listed for Block
#  have the value No_Block.

# Property:	Block
#
# @missing: 0000..10FFFF; No_Block
#

"""


def md_to_txt():
    block_list = []
    with open(md_dir, "r", encoding="utf-8") as md_file:
        lines = md_file.readlines()
        for line in lines:
            if "U+" in line:
                block_match = re.search(r"- (.*?): U\+(.*?)–U\+(.*?)・(.*?)\n", line)
                if block_match:
                    block_en, block_start, block_end, block_zh = block_match.groups()
                    block_list.append(
                        [int(block_start, 16), f"{block_start}..{block_end}; {block_start}{block_zh}|{block_en}"]
                    )

    with open(md2_dir, "r", encoding="utf-8") as md_file:
        lines = md_file.readlines()
        for line in lines:
            if "U+" in line:
                block_match = re.search(r"- (.*?): \[U\+(.*?)–U\+(.*?)\]・(.*?)\n", line)
                if block_match:
                    block_en, block_start, block_end, block_zh = block_match.groups()
                    block_list.append(
                        [int(block_start, 16), f"{block_start}..{block_end}; 〓{block_start}{block_zh}|{block_en}"]
                    )

    block_list.sort(key=lambda x: x[0])
    with open(txt_dir, "w", encoding="utf-8") as txt_file:
        txt_file.write(start)
        for block in block_list:
            txt_file.write(block[1] + "\n")
        txt_file.write("\n# EOF\n")


md_to_txt()
