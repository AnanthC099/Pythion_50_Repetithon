"""
Script to generate a PDF document describing the code structure
of the Pythion_50_Repetithon repository using reportlab.
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
        "Code_Structure_Documentation.pdf"
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
        fontSize=13, textColor=HexColor("#1E3C78"),
        spaceBefore=14, spaceAfter=6,
        backColor=HexColor("#E6EEFA"),
        borderPadding=(4, 4, 4, 4),
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
    code_style = ParagraphStyle(
        "CodeBlock", parent=styles["Code"],
        fontSize=8, leading=11, textColor=HexColor("#282828"),
        backColor=HexColor("#F4F4F4"),
        borderPadding=(6, 6, 6, 6),
        spaceAfter=6,
    )
    stat_label = ParagraphStyle(
        "StatLabel", parent=styles["Normal"],
        fontSize=9, textColor=HexColor("#282828"), leading=13,
    )
    stat_value = ParagraphStyle(
        "StatValue", parent=styles["Normal"],
        fontSize=9, textColor=HexColor("#1E3C78"), leading=13,
    )
    highlight_path_style = ParagraphStyle(
        "HLPath", parent=styles["Code"],
        fontSize=8, textColor=HexColor("#006400"),
        spaceAfter=2, leftIndent=8,
    )
    highlight_desc_style = ParagraphStyle(
        "HLDesc", parent=styles["Normal"],
        fontSize=9, textColor=HexColor("#3C3C3C"),
        leftIndent=8, spaceAfter=8, leading=13,
    )

    story = []

    def file_entry(name, desc):
        story.append(Paragraph(
            f'<font face="Courier" color="#006400">{name}</font>'
            f'&nbsp;&nbsp;-&nbsp;&nbsp;{desc}',
            file_style
        ))

    def bullet(text):
        story.append(Paragraph(f"<bullet>&bull;</bullet> {text}", bullet_style))

    # ── Title Page ────────────────────────────────────────────────────
    story.append(Spacer(1, 40 * mm))
    story.append(Paragraph("Pythion 50 Repetithon", title_style))
    story.append(Paragraph("Complete Code Structure Documentation", subtitle_style))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<i>CoreCode Programming Academy - Python Masterclass</i>",
        ParagraphStyle("sub2", parent=subtitle_style, fontSize=10,
                       textColor=HexColor("#777777"))
    ))
    story.append(Spacer(1, 15 * mm))

    story.append(Paragraph("<b>Project Overview</b>", ParagraphStyle(
        "OverviewH", parent=body_style, fontSize=11, textColor=HexColor("#282828"),
        spaceAfter=4,
    )))
    story.append(Paragraph(
        'This repository is a comprehensive Python programming masterclass called '
        '"Pythion 50 Repetithon", organized into 85 sequential learning sessions '
        '(SESSION_006 through SESSION-092). It covers fundamentals through advanced '
        'topics including OOP, functional programming, closures, GUI development, '
        'and more.',
        body_style
    ))
    story.append(Spacer(1, 8 * mm))

    # Stats table
    story.append(Paragraph("<b>Project Statistics</b>", ParagraphStyle(
        "StatsH", parent=body_style, fontSize=11, textColor=HexColor("#282828"),
        spaceAfter=6,
    )))
    stats = [
        ("Total Files", "213+"),
        ("Python Files", "162"),
        ("PDF Documents", "15"),
        ("PowerPoint Presentations", "2"),
        ("Text Documentation Files", "20+"),
        ("Session Directories", "72"),
        ("Tkinter GUI Examples", "11"),
    ]
    stat_data = [[Paragraph(f"<b>{l}</b>", stat_label), Paragraph(v, stat_value)]
                 for l, v in stats]
    t = Table(stat_data, colWidths=[55 * mm, 30 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [HexColor("#FFFFFF"), HexColor("#F5F8FD")]),
    ]))
    story.append(t)

    # ── Page 2: Top-Level Layout ──────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("1. Top-Level Directory Layout", section_style))
    tree_text = (
        "Pythion_50_Repetithon/<br/>"
        "|-- GUI_USING_TKINTER/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11 Tkinter GUI example scripts<br/>"
        "|-- OPEN_FOR_ALL_WEEK/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Course materials &amp; demonstrations<br/>"
        "|-- SESSION_006/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Early session (basics)<br/>"
        "|-- SESSION_007/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Early session (operators)<br/>"
        "|-- SESSION-008/ ... SESSION-092/&nbsp;&nbsp;70 session directories<br/>"
        "|-- _BLANK_FOLDERS/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Archived empty session folders<br/>"
        "|-- ___All_Errors.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Log of files that failed to download<br/>"
    )
    story.append(Paragraph(tree_text, code_style))
    story.append(Spacer(1, 4 * mm))

    # ── GUI_USING_TKINTER ─────────────────────────────────────────────
    story.append(Paragraph("2. GUI_USING_TKINTER/", section_style))
    story.append(Paragraph(
        "Contains 11 Python scripts demonstrating progressive Tkinter GUI "
        "programming, from basic widgets to a complete multi-frame admission "
        "form application.",
        body_style
    ))
    gui_files = [
        ("01_widget_demo.py", "Basic Tkinter widget demonstration (Label, Entry, Button)"),
        ("02_padx_pady_demo.py", "Layout management with padding and spacing"),
        ("03_textvariable_demo.py", "Text variable binding with StringVar/IntVar"),
        ("04_feet_to_meter.py", "Unit conversion GUI with real-time calculation"),
        ("05_compute_gravitational_gui.py", "Physics gravitational force calculator GUI"),
        ("06_variables_type.py", "Tkinter variable type examples (BooleanVar, etc.)"),
        ("07_check_box_demo.py", "Checkbox (Checkbutton) widget examples"),
        ("08_combo_box_demo.py", "Dropdown / Combobox widget examples"),
        ("09_radio_button.py", "Radio button group selection examples"),
        ("10_cpa_admission_form.py",
         "Complex multi-frame admission form with 5 courses, radio buttons, "
         "checkboxes, and registration logic"),
        ("11_menu_demo.py", "Menu bar and dropdown menu items"),
    ]
    for fname, desc in gui_files:
        file_entry(fname, desc)
    story.append(Spacer(1, 4 * mm))

    # ── OPEN_FOR_ALL_WEEK ─────────────────────────────────────────────
    story.append(Paragraph("3. OPEN_FOR_ALL_WEEK/", section_style))
    story.append(Paragraph(
        "The largest directory (~40 MB). Contains course materials, instructor "
        "resources, demonstration code, and the Python installer for students.",
        body_style
    ))

    story.append(Paragraph("3a. DEMONSTRATION_CODE/", subsection_style))
    story.append(Paragraph(
        "Advanced Python demonstration scripts used in live sessions.",
        body_style
    ))
    demo_files = [
        ("abc_implementation.py",
         "Abstract base class implementation using a custom metaclass named "
         "'interface'; demonstrates abstract method enforcement and inheritance"),
        ("logger.py",
         "Function decorator that logs calls, arguments, return values, "
         "and exceptions to a file"),
        ("test_logger.py",
         "Test suite for the logger decorator with multiple functions "
         "including recursive calls"),
        ("GUI_USING_TKINTER/",
         "Duplicate copy of the top-level Tkinter examples"),
    ]
    for fname, desc in demo_files:
        file_entry(fname, desc)
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("3b. DETAILED_COURSE_CONTENT/", subsection_style))
    file_entry("MASTERCLASS_IN_PYTHON_COURSE_CONTENT.pdf",
               "Complete curriculum PDF covering all 50+ sessions")
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("3c. WEEK_1_MATERIAL/", subsection_style))
    story.append(Paragraph(
        "Foundation PDF documents for the first week of the course.",
        body_style
    ))
    w1_files = [
        ("1_Python_Installation_Guide.pdf", "Step-by-step Python setup instructions"),
        ("2_PythonFileStructure.pdf", "Python file organization concepts"),
        ("3_AssignmentStatementScenarios.pdf", "Assignment statement use cases"),
        ("4_AssignmentStatementAlgorithm.pdf", "Algorithm details for assignment"),
        ("5_DataTypes.pdf", "Data type fundamentals (int, float, str, etc.)"),
    ]
    for fname, desc in w1_files:
        file_entry(fname, desc)
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("3d. IDLE_DOWNLOAD/", subsection_style))
    file_entry("1_Python_Installation_Guide.pdf", "Installation guide (duplicate)")
    file_entry("python-3.13.6-amd64.exe", "Windows Python 3.13.6 installer (28.8 MB)")
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("3e. Root Files in OPEN_FOR_ALL_WEEK/", subsection_style))
    ofa_root = [
        ("CPA_PRESENTATION.pptx", "CoreCode Programming Academy presentation (5.3 MB)"),
        ("Goals_and_definite_chief_aim.pptx", "Goal setting presentation (45 KB)"),
        ("PROFILE - YOGESHWAR SHUKLA.pdf", "Instructor profile document (5.6 MB)"),
        ("The_Definite_Chief_Aim.png", "Goal visualization image (89 KB)"),
    ]
    for fname, desc in ofa_root:
        file_entry(fname, desc)
    story.append(Spacer(1, 4 * mm))

    # ── SESSION DIRECTORIES ───────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("4. Session Directories (SESSION_006 - SESSION-092)", section_style))
    story.append(Paragraph(
        "85 sequential learning sessions forming the core of the course. "
        "Each session directory contains Python scripts, IDLE logs, and/or "
        "PDF materials for that session's topic. Below is a detailed breakdown "
        "organized by learning phase.",
        body_style
    ))

    # Helper for session tables
    def session_table(rows):
        col_w = [28 * mm, 52 * mm, 100 * mm]
        hdr = [
            Paragraph("<b>Session</b>", ParagraphStyle("th", parent=body_style, fontSize=8, textColor=HexColor("#FFFFFF"))),
            Paragraph("<b>Key Files</b>", ParagraphStyle("th2", parent=body_style, fontSize=8, textColor=HexColor("#FFFFFF"))),
            Paragraph("<b>Description</b>", ParagraphStyle("th3", parent=body_style, fontSize=8, textColor=HexColor("#FFFFFF"))),
        ]
        data = [hdr]
        sess_cell = ParagraphStyle("sc", parent=body_style, fontSize=8, textColor=HexColor("#1E3C78"))
        file_cell = ParagraphStyle("fc", parent=body_style, fontSize=7, textColor=HexColor("#006400"), fontName="Courier")
        desc_cell = ParagraphStyle("dc", parent=body_style, fontSize=8, textColor=HexColor("#505050"))
        for s, f, d in rows:
            data.append([
                Paragraph(f"<b>{s}</b>", sess_cell),
                Paragraph(f, file_cell),
                Paragraph(d, desc_cell),
            ])
        tbl = Table(data, colWidths=col_w, repeatRows=1)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), HexColor("#1E3C78")),
            ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#FFFFFF")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FFFFFF"), HexColor("#F5F8FD")]),
            ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#CCCCCC")),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 4 * mm))

    # Phase 1
    story.append(Paragraph("Phase 1: Fundamentals (Sessions 006-021)", subsection_style))
    session_table([
        ("SESSION_006", "BASICS.txt",
         "Fundamental concepts: class vs algorithm, built-in types and functions"),
        ("SESSION_007", "ARITHMETIC-OPERATORS-IDLE-LOG.py, ASCII-CODES-IDLE-LOG.txt",
         "Basic arithmetic operators and ASCII character codes"),
        ("SESSION-008", "01-input-data.py",
         "Basic input/output operations and type conversion (int, float, str)"),
        ("SESSION-009", "01-first-gui-app.py",
         "Introduction to GUI programming with Tkinter"),
        ("SESSION-010", "01-def-statement-demo.py",
         "Function definition basics using the def statement"),
        ("SESSION-011", "3 IDLE log files",
         "Interactive function demonstrations in the IDLE environment"),
        ("SESSION-012", "Session logs",
         "Continued IDLE session practice"),
        ("SESSION-015", "Control flow scripts",
         "Control flow combined with function definitions"),
        ("SESSION-016", "Control flow scripts",
         "Continued control flow practice"),
        ("SESSION-017", "insertion_sort.py + boolean scripts",
         "Boolean operations and the insertion sort algorithm"),
        ("SESSION-018", "01-if-statement.py, 02-if-else-statement.py, 03-if-elif-else-statement.py",
         "Branching statements: if, if-else, if-elif-else patterns"),
        ("SESSION-020", "GUI button demos",
         "Tkinter button widget demonstrations"),
        ("SESSION-021", "Toggle functionality scripts",
         "GUI toggle button and event handling"),
    ])

    # Phase 2
    story.append(Paragraph("Phase 2: Core Programming (Sessions 023-050)", subsection_style))
    session_table([
        ("SESSION-023", "4 files: global vars, GUI squares",
         "Global variables and GUI square-drawing applications"),
        ("SESSION-024", "01-class-demo.py",
         "Class basics: defining a simple Date class with attributes"),
        ("SESSION-025 to 030", "OOP progression scripts",
         "Object-oriented programming: classes, methods, constructors, self"),
        ("SESSION-032 to 045", "Data structure scripts",
         "Data structure and collection handling (lists, tuples, dicts, sets)"),
        ("SESSION-048", "abc.py, pqr.py, xyz.py, show_pwd.py",
         "Small utility scripts and module import examples"),
        ("SESSION-050", "01-create-and-write-on-file.py, 03-file-copy.py, 04-commandline-arguments.py",
         "File I/O: creating, writing, copying files; command-line arguments with sys.argv"),
    ])

    # Phase 3
    story.append(Paragraph("Phase 3: Functional Programming (Sessions 051-077)", subsection_style))
    session_table([
        ("SESSION-051/052", "6 files each",
         "File handling and text processing techniques"),
        ("SESSION-059/060", "SET-IDLE-LOG.py",
         "Set operations: union, intersection, difference, symmetric difference"),
        ("SESSION-063", "LIST-GENERAL-SYNTAX.py, LIST-IDLE-LOG.py, VALIDITY-OF-OPERATOR.py",
         "List operations: indexing, slicing, operators, methods"),
        ("SESSION-064 to 072", "Multiple scripts",
         "Advanced data structures and introduction to functional programming"),
        ("SESSION-073", "LAMBDA-IDLE-LOG.py, power_lambda_map.py + PDFs",
         "Lambda expressions and map() function with lambda"),
        ("SESSION-074", "01-write-demo.py + IDLE-FILTER-LOG.pdf",
         "Filter operations: filter() with lambda and named functions"),
        ("SESSION-076", "List-Comprehension-General-Format-And-Some-Examples.py + PDF",
         "List comprehensions: syntax, single-variable forms (V1 to V4)"),
        ("SESSION-077", "Advanced-List-Comprehension.pdf",
         "Advanced list comprehensions with multiple variables and conditions"),
    ])

    # Phase 4
    story.append(PageBreak())
    story.append(Paragraph("Phase 4: Advanced Functions &amp; Scope (Sessions 079-088)", subsection_style))
    session_table([
        ("SESSION-079", "Nested-Def-Statement/01-def-under-def.py, Language-Topics-Covered-So-Far.txt",
         "Nested function definitions, scope management, and curriculum checklist"),
        ("SESSION-080", "01-nested-def-statement-practice.py, 02-symbol-table.py",
         "Symbol tables and nested def statement practice"),
        ("SESSION-081", "Scope scripts",
         "Python scope rules introduction"),
        ("SESSION-082", "03-LEGB-Scope-Rule.py, 04-UnboundLocalError.py, 05-NameError-FreeVariable.py",
         "LEGB scope rule: Local, Enclosing, Global, Built-in; UnboundLocalError and NameError demos"),
        ("SESSION-084", "04-Solution...global-statement.py, 07-nonlocal-demo.py",
         "Global and nonlocal statements for modifying enclosing scope variables"),
        ("SESSION-085/086", "01-Returning-Function-As-Data-Object.py, 02-FunctionFactory.py",
         "Higher-order functions: returning functions, closures, function factories"),
        ("SESSION-087", "PARAMETER-PASSING-GURU-KILLI.py + PDFs",
         "Parameter passing mechanisms: positional, keyword, *args, **kwargs"),
    ])

    # Phase 5
    story.append(Paragraph("Phase 5: Object-Oriented Programming (Sessions 090-092)", subsection_style))
    session_table([
        ("SESSION-090", "03-Quadrilateral-Version-I.py, GENERAL-SYNTAX.txt",
         "Quadrilateral class Version I: class definition with constructor, attributes for 4 sides and 4 angles"),
        ("SESSION-091", "Quadrilateral full implementation (2 files)",
         "Quadrilateral class complete implementation with methods"),
        ("SESSION-092", "01-Triangle.py, 02-Vector3D.py",
         "Geometric shape classes: Triangle with perimeter/area; Vector3D with add, subtract, normalize, dot/cross product"),
    ])

    # ── _BLANK_FOLDERS ────────────────────────────────────────────────
    story.append(Paragraph("5. _BLANK_FOLDERS/", section_style))
    story.append(Paragraph(
        "Archive of session folders that were initially empty or contained "
        "files that could not be downloaded.",
        body_style
    ))
    bullet("__SESSION-040/ - Originally contained 02-while-else-demo.py (download failed)")
    bullet("__SESSION-041/ - Originally contained while-statement-repeatithon.py (download failed)")
    bullet("__SESSION-043/ - Originally contained class-statement-repeatithon.py (download failed)")
    bullet("__SESSION-049/ - Originally contained abc.txt (download failed)")
    story.append(Spacer(1, 4 * mm))

    # ── ___All_Errors.txt ─────────────────────────────────────────────
    story.append(Paragraph("6. ___All_Errors.txt", section_style))
    story.append(Paragraph(
        "A log file at the repository root tracking files that failed to "
        "download during initial setup. Lists 4 files across sessions 040, "
        "041, 043, and 049 that could not be retrieved.",
        body_style
    ))
    story.append(Spacer(1, 4 * mm))

    # ── Curriculum Progression ────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("7. Curriculum Progression Summary", section_style))
    story.append(Paragraph(
        "The course follows a carefully structured learning path. "
        "Below is the topic progression as documented in the repository.",
        body_style
    ))

    phases = [
        ("Fundamentals (Sessions 006-021)", [
            "Python execution model and memory management",
            "Assignment statements and the object model",
            "Data types: bool, int, float, str, list, tuple, dict, set",
            "Branching: if / elif / else",
            "Looping: while, for, break, continue, pass",
        ]),
        ("Procedural Programming (Sessions 022-050)", [
            "Function definition with def statement",
            "Parameter passing (positional, keyword, defaults)",
            "Type annotations and return values",
            "Exception handling basics",
            "File I/O and command-line arguments",
        ]),
        ("Functional Programming (Sessions 051-077)", [
            "Lambda expressions",
            "Built-in higher-order functions: map(), filter(), reduce()",
            "List comprehensions (single and multi-variable)",
            "Set and dictionary operations",
        ]),
        ("Advanced Functions (Sessions 079-088)", [
            "Nested function definitions",
            "Scope and LEGB rule (Local, Enclosing, Global, Built-in)",
            "global and nonlocal statements",
            "Higher-order functions and closures",
            "Function factories and implicit state saving",
        ]),
        ("Object-Oriented Programming (Sessions 090-092)", [
            "Class definitions with __init__ constructor",
            "Instance attributes and the self parameter",
            "Object and class namespaces",
            "Geometric shape implementations (Quadrilateral, Triangle, Vector3D)",
        ]),
        ("Remaining Topics (Not Yet Covered)", [
            "Operator overloading",
            "Inheritance and polymorphism",
            "Advanced exception handling",
            "Iterators and generators",
            "Context managers and decorators",
            "Metaclasses",
            "Threads, regex, databases, ML/DS applications",
        ]),
    ]

    for title, topics in phases:
        story.append(Paragraph(f"<b>{title}</b>", ParagraphStyle(
            "PhaseH", parent=body_style, fontSize=10,
            textColor=HexColor("#32508C"), spaceBefore=8, spaceAfter=4,
        )))
        for t in topics:
            bullet(t)
        story.append(Spacer(1, 2 * mm))

    # ── Key Code Highlights ───────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("8. Key Code Highlights", section_style))
    story.append(Paragraph(
        "Notable scripts in the repository that demonstrate important concepts:",
        body_style
    ))

    highlights = [
        ("OPEN_FOR_ALL_WEEK/DEMONSTRATION_CODE/abc_implementation.py",
         "Implements abstract base classes using a custom metaclass named 'interface'. "
         "Demonstrates how Python enforces abstract methods through metaclass __call__ "
         "and how inheritance of abstract methods works."),
        ("OPEN_FOR_ALL_WEEK/DEMONSTRATION_CODE/logger.py",
         "A production-style function decorator that logs every function call with "
         "arguments, return values, and exception details to a log file. Shows "
         "decorator pattern and exception handling."),
        ("GUI_USING_TKINTER/10_cpa_admission_form.py",
         "A complex Tkinter application with multiple frames, radio buttons for "
         "5 courses, checkboxes, and a complete registration workflow. Demonstrates "
         "real-world GUI application structure."),
        ("SESSION-092/02-Vector3D.py",
         "A 3D vector class with mathematical operations: addition, subtraction, "
         "normalization, dot product, and cross product. Demonstrates operator "
         "concepts and mathematical programming with classes."),
        ("SESSION-082/03-LEGB-Scope-Rule.py",
         "Comprehensive demonstration of Python's LEGB scope resolution rule with "
         "examples showing Local, Enclosing, Global, and Built-in scope lookups."),
        ("SESSION-085/02-FunctionFactory.py",
         "Demonstrates closures and function factories - functions that create and "
         "return other functions with captured state from the enclosing scope."),
    ]

    for path, desc in highlights:
        story.append(Paragraph(path, highlight_path_style))
        story.append(Paragraph(desc, highlight_desc_style))

    # ── Build PDF ─────────────────────────────────────────────────────
    doc.build(story)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    build_pdf()
