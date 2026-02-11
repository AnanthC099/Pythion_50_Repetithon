"""
Script to generate a PDF document presenting the Pythion 50 Repetithon
curriculum in REVERSE order: from Advanced topics down to Simple fundamentals.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def build_pdf():
    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Advanced_To_Simple_Sequence.pdf"
    )

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
    )

    # ── Styles ────────────────────────────────────────────────────────
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title2", parent=styles["Title"],
        fontSize=22, textColor=HexColor("#1E3C78"),
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle2", parent=styles["Normal"],
        fontSize=13, textColor=HexColor("#555555"),
        alignment=TA_CENTER, spaceAfter=4,
    )
    section_style = ParagraphStyle(
        "Section", parent=styles["Heading2"],
        fontSize=13, textColor=HexColor("#FFFFFF"),
        spaceBefore=14, spaceAfter=6,
        backColor=HexColor("#1E3C78"),
        borderPadding=(6, 6, 6, 6),
    )
    subsection_style = ParagraphStyle(
        "Subsection", parent=styles["Heading3"],
        fontSize=11, textColor=HexColor("#32508C"),
        spaceBefore=10, spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "Body2", parent=styles["Normal"],
        fontSize=9, leading=13, textColor=HexColor("#282828"),
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "Bullet2", parent=styles["Normal"],
        fontSize=9, leading=13, textColor=HexColor("#282828"),
        leftIndent=18, bulletIndent=8, spaceAfter=2,
    )
    file_style = ParagraphStyle(
        "FileEntry", parent=styles["Normal"],
        fontSize=8, leading=12, textColor=HexColor("#333333"),
        leftIndent=12, spaceAfter=2,
    )
    level_label_style = ParagraphStyle(
        "LevelLabel", parent=styles["Normal"],
        fontSize=10, textColor=HexColor("#FFFFFF"),
        alignment=TA_CENTER,
    )
    topic_header_style = ParagraphStyle(
        "TopicHeader", parent=styles["Normal"],
        fontSize=10, textColor=HexColor("#1E3C78"),
        spaceBefore=6, spaceAfter=3,
    )
    session_ref_style = ParagraphStyle(
        "SessionRef", parent=styles["Normal"],
        fontSize=8, textColor=HexColor("#006400"),
        leftIndent=12, spaceAfter=1,
        fontName="Courier",
    )
    desc_style = ParagraphStyle(
        "DescStyle", parent=styles["Normal"],
        fontSize=9, textColor=HexColor("#3C3C3C"),
        leftIndent=12, spaceAfter=6, leading=13,
    )

    story = []

    def bullet(text):
        story.append(Paragraph(f"<bullet>&bull;</bullet> {text}", bullet_style))

    def file_entry(name, desc):
        story.append(Paragraph(
            f'<font face="Courier" color="#006400">{name}</font>'
            f'&nbsp;&nbsp;-&nbsp;&nbsp;{desc}',
            file_style
        ))

    def level_badge(text, color):
        """Create a colored difficulty badge."""
        badge_style = ParagraphStyle(
            "Badge", parent=styles["Normal"],
            fontSize=8, textColor=HexColor("#FFFFFF"),
            backColor=HexColor(color),
            borderPadding=(3, 6, 3, 6),
            alignment=TA_LEFT,
            spaceAfter=4,
        )
        story.append(Paragraph(f"<b>{text}</b>", badge_style))

    # ── Title Page ────────────────────────────────────────────────────
    story.append(Spacer(1, 30 * mm))
    story.append(Paragraph("Pythion 50 Repetithon", title_style))
    story.append(Paragraph(
        "Topic Sequence: Advanced to Simple",
        subtitle_style
    ))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<i>CoreCode Programming Academy - Python Masterclass</i>",
        ParagraphStyle("sub2", parent=subtitle_style, fontSize=10,
                       textColor=HexColor("#777777"))
    ))
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(
        width="60%", thickness=1.5,
        color=HexColor("#1E3C78"), spaceAfter=6, spaceBefore=2,
    ))
    story.append(Spacer(1, 10 * mm))

    story.append(Paragraph(
        "This document presents the entire Python Masterclass curriculum "
        "in <b>reverse order</b> - starting from the most advanced topics "
        "and progressing down to the simplest fundamentals. This sequence "
        "is useful for experienced programmers who want to quickly locate "
        "advanced material, or for reviewing topics from complex to basic.",
        body_style
    ))
    story.append(Spacer(1, 8 * mm))

    # Difficulty legend
    story.append(Paragraph("<b>Difficulty Levels</b>", ParagraphStyle(
        "LegendH", parent=body_style, fontSize=11, textColor=HexColor("#282828"),
        spaceAfter=6,
    )))

    legend_data = [
        [Paragraph('<font color="#FFFFFF"><b>LEVEL 6</b></font>',
                   ParagraphStyle("l6", parent=body_style, fontSize=8, backColor=HexColor("#8B0000"),
                                  textColor=HexColor("#FFFFFF"), borderPadding=(2, 4, 2, 4))),
         Paragraph("Expert - Metaclasses, Abstract Base Classes, Decorators", body_style)],
        [Paragraph('<font color="#FFFFFF"><b>LEVEL 5</b></font>',
                   ParagraphStyle("l5", parent=body_style, fontSize=8, backColor=HexColor("#CC3300"),
                                  textColor=HexColor("#FFFFFF"), borderPadding=(2, 4, 2, 4))),
         Paragraph("Advanced - Closures, Function Factories, LEGB Scope", body_style)],
        [Paragraph('<font color="#FFFFFF"><b>LEVEL 4</b></font>',
                   ParagraphStyle("l4", parent=body_style, fontSize=8, backColor=HexColor("#E06600"),
                                  textColor=HexColor("#FFFFFF"), borderPadding=(2, 4, 2, 4))),
         Paragraph("Upper Intermediate - Lambda, Map/Filter, List Comprehensions", body_style)],
        [Paragraph('<font color="#FFFFFF"><b>LEVEL 3</b></font>',
                   ParagraphStyle("l3", parent=body_style, fontSize=8, backColor=HexColor("#CC9900"),
                                  textColor=HexColor("#FFFFFF"), borderPadding=(2, 4, 2, 4))),
         Paragraph("Intermediate - OOP, File I/O, Data Structures", body_style)],
        [Paragraph('<font color="#FFFFFF"><b>LEVEL 2</b></font>',
                   ParagraphStyle("l2", parent=body_style, fontSize=8, backColor=HexColor("#339966"),
                                  textColor=HexColor("#FFFFFF"), borderPadding=(2, 4, 2, 4))),
         Paragraph("Core - Functions, Control Flow, Branching", body_style)],
        [Paragraph('<font color="#FFFFFF"><b>LEVEL 1</b></font>',
                   ParagraphStyle("l1", parent=body_style, fontSize=8, backColor=HexColor("#336699"),
                                  textColor=HexColor("#FFFFFF"), borderPadding=(2, 4, 2, 4))),
         Paragraph("Beginner - Variables, Data Types, Input/Output, Setup", body_style)],
    ]
    legend_tbl = Table(legend_data, colWidths=[25 * mm, 145 * mm])
    legend_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [HexColor("#FAFAFA"), HexColor("#FFFFFF")]),
    ]))
    story.append(legend_tbl)

    # ══════════════════════════════════════════════════════════════════
    # LEVEL 6: EXPERT
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "LEVEL 6 - EXPERT: Metaclasses, Abstract Base Classes &amp; Decorators",
        section_style
    ))
    story.append(Paragraph(
        "The most advanced concepts in the curriculum. These topics require "
        "a deep understanding of Python's object model, function internals, "
        "and metaprogramming capabilities.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # Topic 1: Metaclasses & ABC
    story.append(Paragraph("<b>1. Metaclasses &amp; Abstract Base Classes</b>", topic_header_style))
    story.append(Paragraph("DEMONSTRATION_CODE/abc_implementation.py", session_ref_style))
    story.append(Paragraph(
        "Custom metaclass named 'interface' that enforces abstract method implementation. "
        "Demonstrates how Python's metaclass __call__ mechanism can be used to prevent "
        "instantiation of classes with unimplemented abstract methods. Requires understanding "
        "of type(), __call__, and the class creation process.",
        desc_style
    ))

    # Topic 2: Decorators
    story.append(Paragraph("<b>2. Function Decorators (Production-Style)</b>", topic_header_style))
    story.append(Paragraph("DEMONSTRATION_CODE/logger.py, test_logger.py", session_ref_style))
    story.append(Paragraph(
        "A production-quality function decorator that wraps functions to log every call "
        "with arguments, return values, and exception details to a file. Demonstrates "
        "the decorator pattern, *args/**kwargs forwarding, exception handling in "
        "wrappers, and file-based logging. Includes test suite with recursive call "
        "demonstrations.",
        desc_style
    ))

    # Topic 3: Geometric classes with math
    story.append(Paragraph("<b>3. Advanced Class Design - Vector3D</b>", topic_header_style))
    story.append(Paragraph("SESSION-092/02-Vector3D.py", session_ref_style))
    story.append(Paragraph(
        "A 3D vector class implementing mathematical operations: addition, subtraction, "
        "normalization, dot product, and cross product. Demonstrates operator concepts, "
        "mathematical programming, type validation in constructors, and complex method "
        "implementations with geometric algorithms.",
        desc_style
    ))

    # Topic 4: Triangle class
    story.append(Paragraph("<b>4. Advanced Class Design - Triangle</b>", topic_header_style))
    story.append(Paragraph("SESSION-092/01-Triangle.py", session_ref_style))
    story.append(Paragraph(
        "Triangle class with perimeter and area calculations using Heron's formula. "
        "Includes constructor validation for triangle inequality, type checking, "
        "and mathematical computation methods.",
        desc_style
    ))

    # Topic 5: Code Object Verification
    story.append(Paragraph("<b>5. Code Object Verification &amp; Attribute Management</b>", topic_header_style))
    story.append(Paragraph("SESSION-079/CODE-OBJECT-VERIFICATION-ATTRIBUTE-MANAGEMENT-EXAMPLE.pdf", session_ref_style))
    story.append(Paragraph(
        "Deep analysis of Python's code objects, attribute management mechanisms, "
        "and verification techniques. Explores the internal structure of function "
        "and class objects.",
        desc_style
    ))

    # ══════════════════════════════════════════════════════════════════
    # LEVEL 5: ADVANCED
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "LEVEL 5 - ADVANCED: Closures, Function Factories &amp; Scope Mastery",
        section_style
    ))
    story.append(Paragraph(
        "Advanced function behavior including closures, higher-order functions that "
        "return functions, scope resolution mastery, and complex parameter passing. "
        "Sessions 079-088.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # Topic 6: Closures & Function Factories
    story.append(Paragraph("<b>6. Closures &amp; Function Factories</b>", topic_header_style))
    story.append(Paragraph("SESSION-085/01-Returning-Function-As-If-It-Were-A-Data-Object.py", session_ref_style))
    story.append(Paragraph("SESSION-086/02-FunctionFactory.py", session_ref_style))
    story.append(Paragraph("SESSION-085/IDLE-LOG.pdf", session_ref_style))
    story.append(Paragraph(
        "Functions that create and return other functions with captured state from "
        "the enclosing scope. Demonstrates implicit state saving through closures, "
        "function factories that generate specialized functions, and treating "
        "functions as first-class data objects.",
        desc_style
    ))

    # Topic 7: LEGB Scope Rule
    story.append(Paragraph("<b>7. LEGB Scope Rule - Complete Mastery</b>", topic_header_style))
    story.append(Paragraph("SESSION-082/03-LEGB-Scope-Rule.py", session_ref_style))
    story.append(Paragraph("SESSION-082/04-UnboundLocalError.py", session_ref_style))
    story.append(Paragraph("SESSION-082/05-NameError-FreeVariable.py", session_ref_style))
    story.append(Paragraph(
        "Comprehensive demonstration of Python's LEGB scope resolution: Local, "
        "Enclosing, Global, Built-in. Includes analysis of UnboundLocalError "
        "scenarios, free variable behavior, NameError conditions, and how Python "
        "resolves variable references at each scope level.",
        desc_style
    ))

    # Topic 8: global and nonlocal
    story.append(Paragraph("<b>8. global &amp; nonlocal Statements</b>", topic_header_style))
    story.append(Paragraph("SESSION-084/04-Solution-to-Scenario-1-using-global-statement.py", session_ref_style))
    story.append(Paragraph("SESSION-084/07-nonlocal-demo.py", session_ref_style))
    story.append(Paragraph(
        "Using global and nonlocal statements to modify variables in enclosing "
        "scopes. Demonstrates when and why these statements are needed, "
        "the problems they solve, and their interaction with nested function "
        "definitions.",
        desc_style
    ))

    # Topic 9: Parameter Passing
    story.append(Paragraph("<b>9. Advanced Parameter Passing (*args, **kwargs)</b>", topic_header_style))
    story.append(Paragraph("SESSION-087/PARAMETER-PASSING-GURU-KILLI.py", session_ref_style))
    story.append(Paragraph("SESSION-087/PARAMETER-PASSING-IDLE-LOG.pdf", session_ref_style))
    story.append(Paragraph("SESSION-087/REALLY-BIG-PICTURE.pdf", session_ref_style))
    story.append(Paragraph("SESSION-088/Non-Default-After-Default-IDLE-LOG.pdf", session_ref_style))
    story.append(Paragraph(
        "Complete parameter passing mechanisms: positional arguments, keyword "
        "arguments, default values, *args for variable positional arguments, "
        "**kwargs for variable keyword arguments, and the rules governing their "
        "ordering. Includes the 'Really Big Picture' overview document.",
        desc_style
    ))

    # Topic 10: Nested Defs
    story.append(Paragraph("<b>10. Nested Function Definitions</b>", topic_header_style))
    story.append(Paragraph("SESSION-079/Nested-Def-Statement/01-def-under-def.py", session_ref_style))
    story.append(Paragraph("SESSION-080/01-nested-def-statement-practice.py", session_ref_style))
    story.append(Paragraph("SESSION-080/02-symbol-table.py", session_ref_style))
    story.append(Paragraph(
        "Defining functions within functions. Covers inner function access to "
        "enclosing scope variables, symbol table analysis, and the foundation "
        "for understanding closures.",
        desc_style
    ))

    # Topic 11: Exception Handling
    story.append(Paragraph("<b>11. Exception Handling (try/except)</b>", topic_header_style))
    story.append(Paragraph("SESSION-088 / Various session scripts", session_ref_style))
    story.append(Paragraph(
        "Handling runtime errors with try/except blocks. Catching specific "
        "exception types, understanding the exception hierarchy, and using "
        "exception handling in production-style code.",
        desc_style
    ))

    # ══════════════════════════════════════════════════════════════════
    # LEVEL 4: UPPER INTERMEDIATE
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "LEVEL 4 - UPPER INTERMEDIATE: Functional Programming Concepts",
        section_style
    ))
    story.append(Paragraph(
        "Functional programming patterns including lambda expressions, "
        "higher-order functions, and list comprehensions. Sessions 051-077.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # Topic 12: Advanced List Comprehensions
    story.append(Paragraph("<b>12. Advanced List Comprehensions (Multi-Variable)</b>", topic_header_style))
    story.append(Paragraph("SESSION-077/Advanced-List-Comprehension.pdf", session_ref_style))
    story.append(Paragraph(
        "Multi-variable list comprehensions with nested iterations, "
        "conditional filters, and complex expressions. Extends single-variable "
        "comprehensions to handle multiple iterables and compound conditions.",
        desc_style
    ))

    # Topic 13: Single-Variable List Comprehensions
    story.append(Paragraph("<b>13. List Comprehensions (Single-Variable, V1-V4)</b>", topic_header_style))
    story.append(Paragraph("SESSION-076/List-Comprehension-General-Format-And-Some-Examples.py", session_ref_style))
    story.append(Paragraph("SESSION-076/SINGLE-VARIABLE-LIST-COMPREHENSION-V1-TO-V4.pdf", session_ref_style))
    story.append(Paragraph(
        "General syntax and four progressive versions of single-variable list "
        "comprehensions. From basic [expr for x in iterable] to filtered forms "
        "with conditions.",
        desc_style
    ))

    # Topic 14: Lambda + Map
    story.append(Paragraph("<b>14. Lambda Expressions &amp; map() Function</b>", topic_header_style))
    story.append(Paragraph("SESSION-073/LAMBDA-IDLE-LOG.py", session_ref_style))
    story.append(Paragraph("SESSION-073/power_lambda_map.py", session_ref_style))
    story.append(Paragraph("SESSION-073/LAMBDA-IDLE-LOG-FINAL.pdf, MAP-IDLE-LOG.pdf", session_ref_style))
    story.append(Paragraph(
        "Anonymous functions using lambda syntax. Using map() to apply "
        "functions across iterables. Combining lambda with map for concise "
        "data transformations.",
        desc_style
    ))

    # Topic 15: Filter
    story.append(Paragraph("<b>15. filter() Function</b>", topic_header_style))
    story.append(Paragraph("SESSION-074/IDLE-FILTER-LOG.pdf", session_ref_style))
    story.append(Paragraph("SESSION-074/01-write-demo.py", session_ref_style))
    story.append(Paragraph(
        "Using filter() with lambda and named functions to select elements "
        "from iterables based on conditions. Comparison with list "
        "comprehension filtering.",
        desc_style
    ))

    # Topic 16: reduce()
    story.append(Paragraph("<b>16. reduce() Function</b>", topic_header_style))
    story.append(Paragraph("SESSION-073 to 077 / Functional programming sessions", session_ref_style))
    story.append(Paragraph(
        "Reducing iterables to single values using functools.reduce(). "
        "Accumulation patterns and comparison with explicit loops.",
        desc_style
    ))

    # Topic 17: Set Operations
    story.append(Paragraph("<b>17. Set Operations</b>", topic_header_style))
    story.append(Paragraph("SESSION-059/SET-IDLE-LOG.py", session_ref_style))
    story.append(Paragraph("SESSION-060/ Set continuation scripts", session_ref_style))
    story.append(Paragraph(
        "Set data structure operations: union, intersection, difference, "
        "and symmetric difference. Set membership testing and mathematical "
        "set theory applied to Python.",
        desc_style
    ))

    # Topic 18: File Handling & Text Processing
    story.append(Paragraph("<b>18. File Handling &amp; Text Processing</b>", topic_header_style))
    story.append(Paragraph("SESSION-051/052 / 6 files each", session_ref_style))
    story.append(Paragraph(
        "Advanced file handling techniques and text processing. Reading, "
        "writing, and manipulating text data from files.",
        desc_style
    ))

    # ══════════════════════════════════════════════════════════════════
    # LEVEL 3: INTERMEDIATE
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "LEVEL 3 - INTERMEDIATE: OOP, Data Structures &amp; File I/O",
        section_style
    ))
    story.append(Paragraph(
        "Object-oriented programming basics, complex data structures, "
        "file operations, and GUI development. Sessions 023-050.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # Topic 19: Quadrilateral Class
    story.append(Paragraph("<b>19. OOP - Quadrilateral Class</b>", topic_header_style))
    story.append(Paragraph("SESSION-090/03-Quadrilateral-Version-I.py", session_ref_style))
    story.append(Paragraph("SESSION-091/01-Quadrilateral.py, 02-Quadrilateral.py", session_ref_style))
    story.append(Paragraph(
        "Quadrilateral class with constructor accepting 4 sides and 4 angles. "
        "Includes validation, instance attributes, and progressive "
        "version improvements across sessions.",
        desc_style
    ))

    # Topic 20: Class & OOP Basics
    story.append(Paragraph("<b>20. Class Definitions, Constructors &amp; Methods</b>", topic_header_style))
    story.append(Paragraph("SESSION-024/01-class-demo.py", session_ref_style))
    story.append(Paragraph("SESSION-025/01-class-date-complete.py", session_ref_style))
    story.append(Paragraph("SESSION-025 to 030 / OOP progression scripts", session_ref_style))
    story.append(Paragraph(
        "Defining classes with the class statement, __init__ constructors, "
        "instance attributes, the self parameter, methods, and object "
        "instantiation. Progressive examples building a Date class.",
        desc_style
    ))

    # Topic 21: Complex GUI
    story.append(Paragraph("<b>21. Complex GUI Applications (Tkinter)</b>", topic_header_style))
    story.append(Paragraph("GUI_USING_TKINTER/10_cpa_admission_form.py", session_ref_style))
    story.append(Paragraph(
        "Complex multi-frame Tkinter application with 5 course selection "
        "radio buttons, checkbox groups, and a complete registration workflow "
        "with validation. Demonstrates real-world GUI application structure.",
        desc_style
    ))

    # Topic 22: File I/O & CLI
    story.append(Paragraph("<b>22. File I/O &amp; Command-Line Arguments</b>", topic_header_style))
    story.append(Paragraph("SESSION-050/01-create-and-write-on-file.py", session_ref_style))
    story.append(Paragraph("SESSION-050/03-file-copy.py", session_ref_style))
    story.append(Paragraph("SESSION-050/04-commandline-arguments.py", session_ref_style))
    story.append(Paragraph(
        "Creating, writing, and copying files. Using sys.argv to accept "
        "command-line arguments. File modes and file object methods.",
        desc_style
    ))

    # Topic 23: Lists, Tuples, Dicts
    story.append(Paragraph("<b>23. Data Structures: Lists, Tuples, Dictionaries</b>", topic_header_style))
    story.append(Paragraph("SESSION-032 to 045 / Data structure scripts", session_ref_style))
    story.append(Paragraph("SESSION-063/LIST-GENERAL-SYNTAX.py, LIST-IDLE-LOG.py", session_ref_style))
    story.append(Paragraph(
        "List operations (indexing, slicing, append, extend, pop, insert), "
        "tuple immutability and packing/unpacking, dictionary key-value "
        "operations, and comparative use cases for each structure.",
        desc_style
    ))

    # Topic 24: Global Variables
    story.append(Paragraph("<b>24. Global Variables &amp; Scope Basics</b>", topic_header_style))
    story.append(Paragraph("SESSION-023/global variable scripts", session_ref_style))
    story.append(Paragraph(
        "Introduction to global variables, variable scope within functions, "
        "and the distinction between local and global namespaces.",
        desc_style
    ))

    # Topic 25: GUI widgets
    story.append(Paragraph("<b>25. GUI Widgets: Checkboxes, Comboboxes, Radio Buttons, Menus</b>", topic_header_style))
    story.append(Paragraph("GUI_USING_TKINTER/07_check_box_demo.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/08_combo_box_demo.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/09_radio_button.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/11_menu_demo.py", session_ref_style))
    story.append(Paragraph(
        "Interactive widget types: Checkbutton for multi-select options, "
        "Combobox for dropdown selection, Radiobutton for exclusive choice "
        "groups, and Menu for application menu bars.",
        desc_style
    ))

    # ══════════════════════════════════════════════════════════════════
    # LEVEL 2: CORE
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "LEVEL 2 - CORE: Functions, Control Flow &amp; Branching",
        section_style
    ))
    story.append(Paragraph(
        "Fundamental programming constructs: function definitions, "
        "branching, looping, and basic algorithms. Sessions 010-021.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # Topic 26: Insertion Sort
    story.append(Paragraph("<b>26. Algorithms - Insertion Sort</b>", topic_header_style))
    story.append(Paragraph("SESSION-017/insertion_sort.py", session_ref_style))
    story.append(Paragraph(
        "Implementation of the insertion sort algorithm. Demonstrates "
        "algorithmic thinking with nested loops, comparisons, and "
        "element shifting.",
        desc_style
    ))

    # Topic 27: Boolean Operations
    story.append(Paragraph("<b>27. Boolean Operations &amp; Comparisons</b>", topic_header_style))
    story.append(Paragraph("SESSION-017/boolean scripts", session_ref_style))
    story.append(Paragraph(
        "Boolean logic: and, or, not operators. Comparison operators "
        "(==, !=, &lt;, &gt;, &lt;=, &gt;=). Truthy and falsy values "
        "in Python.",
        desc_style
    ))

    # Topic 28: Branching
    story.append(Paragraph("<b>28. Branching: if / elif / else</b>", topic_header_style))
    story.append(Paragraph("SESSION-018/01-if-statement.py", session_ref_style))
    story.append(Paragraph("SESSION-018/02-if-else-statement.py", session_ref_style))
    story.append(Paragraph("SESSION-018/03-if-elif-else-statement.py", session_ref_style))
    story.append(Paragraph(
        "Conditional execution with if statements, if-else for two-way "
        "branching, and if-elif-else for multi-way branching. Covers "
        "condition evaluation and code block indentation.",
        desc_style
    ))

    # Topic 29: Looping
    story.append(Paragraph("<b>29. Looping: while, for, break, continue, pass</b>", topic_header_style))
    story.append(Paragraph("SESSION-015, 016, 040-041 / Control flow scripts", session_ref_style))
    story.append(Paragraph(
        "Iteration with while and for loops. Loop control statements: "
        "break to exit early, continue to skip iterations, pass as a "
        "placeholder. Iterating over ranges, lists, and other iterables.",
        desc_style
    ))

    # Topic 30: Function Definitions
    story.append(Paragraph("<b>30. Function Definitions (def statement)</b>", topic_header_style))
    story.append(Paragraph("SESSION-010/01-def-statement-demo.py", session_ref_style))
    story.append(Paragraph("SESSION-011/IDLE log files", session_ref_style))
    story.append(Paragraph(
        "Defining reusable functions with def. Parameters and arguments, "
        "return values, function calls, and the basics of code organization "
        "through functions.",
        desc_style
    ))

    # Topic 31: GUI Basics
    story.append(Paragraph("<b>31. GUI Basics: Buttons, Events, Toggles</b>", topic_header_style))
    story.append(Paragraph("SESSION-020/GUI button demos", session_ref_style))
    story.append(Paragraph("SESSION-021/Toggle functionality scripts", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/04_feet_to_meter.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/05_compute_gravitational_gui.py", session_ref_style))
    story.append(Paragraph(
        "Button widgets, event handling, toggle functionality, and "
        "practical calculator GUIs (unit conversion, gravitational "
        "force). Connecting UI elements to Python functions.",
        desc_style
    ))

    # ══════════════════════════════════════════════════════════════════
    # LEVEL 1: BEGINNER
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "LEVEL 1 - BEGINNER: Variables, Data Types, I/O &amp; Setup",
        section_style
    ))
    story.append(Paragraph(
        "The foundation of Python programming. Installation, basic data "
        "types, variables, input/output, and the first GUI application. "
        "Sessions 006-009.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # Topic 32: First GUI App
    story.append(Paragraph("<b>32. First GUI Application</b>", topic_header_style))
    story.append(Paragraph("SESSION-009/01-first-gui-app.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/01_widget_demo.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/02_padx_pady_demo.py", session_ref_style))
    story.append(Paragraph("GUI_USING_TKINTER/03_textvariable_demo.py", session_ref_style))
    story.append(Paragraph(
        "Creating a first Tkinter window. Basic widgets: Label, Entry, "
        "Button. Layout management with padding (padx, pady). Variable "
        "binding with StringVar and IntVar.",
        desc_style
    ))

    # Topic 33: Input/Output
    story.append(Paragraph("<b>33. Input/Output &amp; Type Conversion</b>", topic_header_style))
    story.append(Paragraph("SESSION-008/01-input-data.py", session_ref_style))
    story.append(Paragraph(
        "Reading user input with input(). Displaying output with print(). "
        "Type conversion functions: int(), float(), str(). Getting data "
        "from the user and displaying results.",
        desc_style
    ))

    # Topic 34: Operators & ASCII
    story.append(Paragraph("<b>34. Arithmetic Operators &amp; ASCII Codes</b>", topic_header_style))
    story.append(Paragraph("SESSION_007/ARITHMETIC-OPERATORS-IDLE-LOG.py", session_ref_style))
    story.append(Paragraph("SESSION_007/ASCII-CODES-IDLE-LOG.txt", session_ref_style))
    story.append(Paragraph(
        "Basic arithmetic operators: +, -, *, /, //, %, **. Operator "
        "precedence. ASCII character codes and the ord()/chr() functions.",
        desc_style
    ))

    # Topic 35: Data Types
    story.append(Paragraph("<b>35. Data Types</b>", topic_header_style))
    story.append(Paragraph("SESSION_006/BASICS.txt", session_ref_style))
    story.append(Paragraph("WEEK_1_Material/5_DataTypes.pdf", session_ref_style))
    story.append(Paragraph(
        "Python's built-in data types: bool, int, float, str, list, "
        "tuple, dict, set. Understanding type(), isinstance(), and "
        "dynamic typing.",
        desc_style
    ))

    # Topic 36: Assignment & Variables
    story.append(Paragraph("<b>36. Assignment Statements &amp; Variables</b>", topic_header_style))
    story.append(Paragraph("WEEK_1_Material/3_AssignmentStatementScenarios.pdf", session_ref_style))
    story.append(Paragraph("WEEK_1_Material/4_AssignmentStatementAlgorithm.pdf", session_ref_style))
    story.append(Paragraph(
        "How Python assignment works: binding names to objects. The object "
        "model, reference counting, and memory management. Assignment "
        "scenarios and the algorithm Python follows internally.",
        desc_style
    ))

    # Topic 37: Python Setup
    story.append(Paragraph("<b>37. Python Installation &amp; Setup</b>", topic_header_style))
    story.append(Paragraph("WEEK_1_Material/1_Python_Installation_Guide.pdf", session_ref_style))
    story.append(Paragraph("WEEK_1_Material/2_PythonFileStructure.pdf", session_ref_style))
    story.append(Paragraph("IDLE_DOWNLOAD/python-3.13.6-amd64.exe", session_ref_style))
    story.append(Paragraph(
        "Installing Python on Windows. Understanding Python file structure "
        "and organization. Setting up the IDLE development environment. "
        "The very first step of the learning journey.",
        desc_style
    ))

    # ══════════════════════════════════════════════════════════════════
    # SUMMARY PAGE
    # ══════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(Paragraph(
        "Quick Reference: Complete Sequence (Advanced to Simple)",
        section_style
    ))
    story.append(Spacer(1, 4 * mm))

    summary_items = [
        ("LEVEL 6", "#8B0000", [
            "1. Metaclasses & Abstract Base Classes",
            "2. Function Decorators (Production-Style)",
            "3. Advanced Class Design - Vector3D",
            "4. Advanced Class Design - Triangle",
            "5. Code Object Verification & Attribute Management",
        ]),
        ("LEVEL 5", "#CC3300", [
            "6. Closures & Function Factories",
            "7. LEGB Scope Rule - Complete Mastery",
            "8. global & nonlocal Statements",
            "9. Advanced Parameter Passing (*args, **kwargs)",
            "10. Nested Function Definitions",
            "11. Exception Handling (try/except)",
        ]),
        ("LEVEL 4", "#E06600", [
            "12. Advanced List Comprehensions (Multi-Variable)",
            "13. List Comprehensions (Single-Variable, V1-V4)",
            "14. Lambda Expressions & map() Function",
            "15. filter() Function",
            "16. reduce() Function",
            "17. Set Operations",
            "18. File Handling & Text Processing",
        ]),
        ("LEVEL 3", "#CC9900", [
            "19. OOP - Quadrilateral Class",
            "20. Class Definitions, Constructors & Methods",
            "21. Complex GUI Applications (Tkinter)",
            "22. File I/O & Command-Line Arguments",
            "23. Data Structures: Lists, Tuples, Dictionaries",
            "24. Global Variables & Scope Basics",
            "25. GUI Widgets: Checkboxes, Comboboxes, Radio Buttons, Menus",
        ]),
        ("LEVEL 2", "#339966", [
            "26. Algorithms - Insertion Sort",
            "27. Boolean Operations & Comparisons",
            "28. Branching: if / elif / else",
            "29. Looping: while, for, break, continue, pass",
            "30. Function Definitions (def statement)",
            "31. GUI Basics: Buttons, Events, Toggles",
        ]),
        ("LEVEL 1", "#336699", [
            "32. First GUI Application",
            "33. Input/Output & Type Conversion",
            "34. Arithmetic Operators & ASCII Codes",
            "35. Data Types",
            "36. Assignment Statements & Variables",
            "37. Python Installation & Setup",
        ]),
    ]

    for level, color, topics in summary_items:
        # Level header row
        hdr_style = ParagraphStyle(
            f"sum_{level}", parent=body_style, fontSize=10,
            textColor=HexColor("#FFFFFF"),
            backColor=HexColor(color),
            borderPadding=(4, 6, 4, 6),
            spaceBefore=6, spaceAfter=4,
        )
        story.append(Paragraph(f"<b>{level}</b>", hdr_style))
        for topic in topics:
            bullet(topic)
        story.append(Spacer(1, 2 * mm))

    # ── Footer ────────────────────────────────────────────────────────
    story.append(Spacer(1, 10 * mm))
    story.append(HRFlowable(
        width="100%", thickness=1,
        color=HexColor("#CCCCCC"), spaceAfter=4, spaceBefore=4,
    ))
    story.append(Paragraph(
        "<i>Pythion 50 Repetithon - CoreCode Programming Academy</i><br/>"
        "<i>Instructor: Yogeshwar Shukla</i><br/>"
        "<i>37 topics sequenced from Advanced (Level 6) to Simple (Level 1)</i>",
        ParagraphStyle("Footer", parent=body_style, fontSize=8,
                       textColor=HexColor("#999999"), alignment=TA_CENTER)
    ))

    # ── Build PDF ─────────────────────────────────────────────────────
    doc.build(story)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    build_pdf()
