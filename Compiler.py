# import re
import json
from Parts._1_Lexer import lexer
from Parts._2_Parser import parser

# file = "Compiler.py"
file = "examplecode.py"


with open(file, "r") as file:
    tokens = lexer(file)
    with open("tokens.json", "w") as outfile:
        json.dump(tokens, outfile, indent=4)

    syntax_tree = parser(tokens)
    with open("tree.json", "w") as outfile:
        json.dump(syntax_tree, outfile, indent=4)


# regex_patterns = {
#     r"( {4})+(?!\s*$)": "indentation",
#     r"#.*$": "comment",
#     r"\bcontinue\b": "keyword",
#     r"\bnonlocal\b": "keyword",
#     r"\bfinally\b": "keyword",
#     r"\bassert\b": "keyword",
#     r"\bexcept\b": "keyword",
#     r"\bglobal\b": "keyword",
#     r"\bimport\b": "keyword",
#     r"\blambda\b": "keyword",
#     r"\breturn\b": "keyword",
#     r"\bprint\b": "keyword",  # mabye, mabye not, its still a function name therefore a keyword so....
#     r"\bFalse\b": "keyword",
#     r"\basync\b": "keyword",
#     r"\bawait\b": "keyword",
#     r"\bbreak\b": "keyword",
#     r"\bclass\b": "keyword",
#     r"\braise\b": "keyword",
#     r"\bwhile\b": "keyword",
#     r"\byield\b": "keyword",
#     r"\bNone\b": "keyword",
#     r"\bTrue\b": "keyword",
#     r"\belif\b": "keyword",
#     r"\belse\b": "keyword",
#     r"\bfrom\b": "keyword",
#     r"\bpass\b": "keyword",
#     r"\bwith\b": "keyword",
#     r"\band\b": "keyword",
#     r"\bdef\b": "keyword",
#     r"\bdel\b": "keyword",
#     r"\bfor\b": "keyword",
#     r"\bnot\b": "keyword",
#     r"\btry\b": "keyword",
#     r"\bas\b": "keyword",
#     r"\bif\b": "keyword",
#     r"\bin\b": "keyword",
#     r"\bis\b": "keyword",
#     r"\bor\b": "keyword",
#     r"\+\+": "increment",
#     r"--": "increment",
#     r"\+=": "addition",
#     r"-=": "subtraction",
#     r"\*=": "multiplication",
#     r"/=": "division",
#     r"%=": "modulation",
#     r"\+=": "and_assign",
#     r"-=": "or_assign",
#     r"\*=": "xor_assign",
#     r"==": "equal",
#     r"<=": "less_equal",
#     r">=": "more_equal",
#     r"!=": "not_equal",
#     r"\(": "left_paren",
#     r"\)": "right_paren",
#     r"\{": "left_brace",
#     r"\}": "right_brace",
#     r"\[": "left_bracket",
#     r"\]": "right_bracket",
#     r"<": "more_than",
#     r">": "less_than",
#     r":": "colon",
#     r";": "semicolon",
#     r"\+": "addition",
#     r"-": "subtraction",
#     r"\*": "multiplication",
#     r"/": "division",
#     r"%": "modulo",
#     r"=": "assign",
#     r"!": "not",
#     r"~": "invert",
#     r"^-?\d*\.\d+": "float",
#     r"^-?\d+": "integer",
#     r"\.": "period",
#     r",": "comma",
#     r"(?:\'(?:[^\'\\]|\\.)*\'|\"(?:[^\"\\]|\\.)*\")": "string",
# }


# def lexer(file_content):
#     tokens = []
#     lines = file_content.split("\n")

#     for line_number, line in enumerate(lines, 1):
#         offset = 0
#         while offset < len(line):
#             match_found = False
#             for regex, token_type in regex_patterns.items():
#                 match = re.match(regex, line[offset:])
#                 if match:
#                     match_found = True
#                     if token_type == "indentation":
#                         tokens.append(
#                             {
#                                 "type": token_type,
#                                 "value": f"{len(match.group()) // 4}",
#                                 "line": f"{line_number}",
#                             }
#                         )
#                     else:
#                         tokens.append(
#                             {
#                                 "type": token_type,
#                                 "value": match.group(),
#                                 "line": f"{line_number}",
#                             }
#                         )
#                     offset += len(match.group())
#                     break

#             if not match_found:  # not a standard regex, probably an identifier
#                 match = re.match(r"\b[A-Za-z_][A-Za-z0-9_]*\b", line[offset:])
#                 if match:
#                     tokens.append(
#                         {
#                             "type": "identifier",
#                             "value": match.group(),
#                             "line": f"{line_number}",
#                         }
#                     )
#                     offset += len(match.group())
#                 else:
#                     if line[offset : offset + 1] != " ":
#                         print(
#                             f"WHAT IS THIS line {line_number}: ({line[offset:offset+1]}) in {line}"
#                         )
#                     offset += 1
#         tokens.append(
#             {
#                 "type": "newline",
#                 "value": "\n",
#                 "line": f"{line_number}",
#             }
#         )
#     return tokens


# def parser(tokens: dict, tab_expected: int = 0):
#     token_number = 0
#     tab_count = 0
#     parse_tree = []

#     while token_number < len(tokens):

#         if tokens[token_number]["type"] == "newline":
#             tab_count = 0

#         elif tokens[token_number]["type"] == "indentation":
#             tab_count = int(tokens[token_number]["value"])

#         elif (
#             tokens[token_number]["type"] == "keyword"
#             and tokens[token_number]["value"]
#             not in (
#                 "and",
#                 "not",
#                 "in",
#                 "is",
#                 "or",
#             )
#         ) and tab_count == tab_expected:

#             current_line = tokens[token_number]["line"]

#             if tokens[token_number]["value"] == "def":  # FUNCTION

#                 function_name = tokens[token_number + 1]["value"]
#                 function_parameters = []
#                 param_count = 0

#                 if tokens[token_number + 3]["type"] == "identifier":  # deal with params

#                     while tokens[token_number + 3 + param_count][
#                         "line"
#                     ] == current_line and (
#                         tokens[token_number + 3 + param_count]["type"] == "identifier"
#                         or tokens[token_number + 3 + param_count]["type"] == "comma"
#                     ):

#                         if (
#                             tokens[token_number + 3 + param_count]["type"]
#                             == "identifier"
#                         ):
#                             # try else statement to test for "value", also for "type"
#                             label = tokens[token_number + 3 + param_count]["value"]
#                             function_parameters.append(
#                                 {"label": label, "type": "integer", "value": None}
#                             )

#                         param_count += 1

#                 function_body = parser(
#                     tokens[token_number + 3 + param_count + 3 :], tab_count + 1
#                 )

#                 parse_tree.append(
#                     {
#                         "function_declaration": {
#                             "name": function_name,
#                             "parameters": function_parameters,
#                             "body": function_body,
#                         }
#                     }
#                 )

#             elif (
#                 tokens[token_number]["value"] == "if" and tab_count == tab_expected
#             ):  # IF STATEMENT
#                 current_line = tokens[token_number]["line"]
#                 if_conditions_tokens = []
#                 cond_count = 0

#                 while tokens[token_number + 1 + cond_count]["type"] != "colon":
#                     if_conditions_tokens.append(tokens[token_number + 1 + cond_count])
#                     cond_count += 1

#                 if_conditions_tokens.append(
#                     tokens[token_number + 1 + cond_count]
#                 )  # append colon
#                 if_conditions_tokens.append(
#                     tokens[token_number + 1 + cond_count + 1]
#                 )  # append newline

#                 conditions = []

#                 while int((len(if_conditions_tokens[:-2]) + 1) / 4) != 0:

#                     if if_conditions_tokens[1]["type"] in (
#                         "equal",
#                         "less_equal",
#                         "more_equal",
#                         "not_equal",
#                         "more_than",
#                         "less_than",
#                     ):
#                         cond_type = if_conditions_tokens[1]["type"]
#                     elif if_conditions_tokens[1][
#                         "type"
#                     ] == "keyword" and if_conditions_tokens[1]["value"] in (
#                         "and",
#                         "not",
#                         "in",
#                         "is",
#                         "or",
#                     ):
#                         cond_type = if_conditions_tokens[1]["value"]
#                     conditions.append(
#                         {
#                             "type": cond_type,
#                             "left": {
#                                 if_conditions_tokens[0]["type"]: if_conditions_tokens[
#                                     0
#                                 ]["value"]
#                             },
#                             "right": {
#                                 if_conditions_tokens[2]["type"]: if_conditions_tokens[
#                                     2
#                                 ]["value"]
#                             },
#                         }
#                     )
#                     if_conditions_tokens = if_conditions_tokens[4:]

#                 then_condition = parser(
#                     tokens[token_number + 1 + cond_count :], tab_count + 1
#                 )

#                 parse_tree.append(
#                     {
#                         "if": {
#                             "condition": conditions,
#                             #     {
#                             #     "type": cond_type,
#                             #     "left": {
#                             #         if_conditions_tokens[0][
#                             #             "type"
#                             #         ]: if_conditions_tokens[0]["value"]
#                             #     },
#                             #     "right": {
#                             #         if_conditions_tokens[2][
#                             #             "type"
#                             #         ]: if_conditions_tokens[2]["value"]
#                             #     },
#                             # },
#                             "then": then_condition,
#                         }
#                     }
#                 )
#         elif tokens[token_number]["type"] == "identifier":  # Function call / assign
#             pass

#         token_number += 1

#     return parse_tree
