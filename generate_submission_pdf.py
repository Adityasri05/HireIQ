import os
from fpdf import FPDF

class HireviumWhitepaper(FPDF):
    def header(self):
        if self.page_no() == 1:
            return  # Suppress header on cover page
            
        # Draw thin brand line at the top
        self.set_fill_color(37, 99, 235)  # Cobalt Blue
        self.rect(0, 0, 210, 4, 'F')
        
        # Header text
        self.set_font("helvetica", "B", 8)
        self.set_text_color(100, 116, 139)  # Slate Gray
        self.cell(0, 10, "HIREVIUM - AI HIRING INTELLIGENCE OPERATING SYSTEM", new_x="RIGHT", new_y="TOP", align="L")
        
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, "HACKATHON SUBMISSION WHITEPAPER", new_x="LMARGIN", new_y="NEXT", align="R")
        
        # Subtle divider line
        self.set_draw_color(226, 232, 240)  # Light gray
        self.line(20, 15, 190, 15)
        self.ln(5)

    def footer(self):
        if self.page_no() == 1:
            return  # Suppress footer on cover page
            
        # Subtle divider line at footer
        self.set_draw_color(226, 232, 240)
        self.line(20, 280, 190, 280)
        
        self.set_y(-15)
        self.set_font("helvetica", "", 8)
        self.set_text_color(100, 116, 139)
        self.cell(0, 10, "Confidential - Adityasri05/Hirevium", new_x="RIGHT", new_y="TOP", align="L")
        
        # Page numbering
        page_num = f"Page {self.page_no()} of {{nb}}"
        self.cell(0, 10, page_num, new_x="LMARGIN", new_y="NEXT", align="R")

    def section_header(self, title):
        self.ln(6)
        self.set_font("helvetica", "B", 14)
        self.set_text_color(37, 99, 235)  # Cobalt Blue
        self.cell(0, 8, title.upper(), new_x="LMARGIN", new_y="NEXT", align="L")
        
        # Draw a small secondary colored bar under the header
        self.set_fill_color(6, 182, 212)  # Cyber Teal
        self.rect(self.get_x(), self.get_y(), 30, 2, 'F')
        self.ln(4)

    def subsection_header(self, title):
        self.ln(4)
        self.set_font("helvetica", "B", 11)
        self.set_text_color(15, 23, 42)  # Slate 900
        self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(2)

    def p(self, text):
        self.set_font("helvetica", "", 9.5)
        self.set_text_color(51, 65, 85)  # Slate 700
        self.multi_cell(0, 5, text)
        self.ln(3)

    def bullet(self, title, desc):
        self.set_font("helvetica", "B", 9.5)
        self.set_text_color(15, 23, 42)
        self.write(5, "-  " + title + ": ")
        self.set_font("helvetica", "", 9.5)
        self.set_text_color(51, 65, 85)
        self.write(5, desc + "\n")
        self.ln(2)

    def draw_callout(self, text):
        self.ln(2)
        # Save positions
        x = self.get_x()
        y = self.get_y()
        
        self.set_font("helvetica", "I", 9.5)
        self.set_text_color(30, 41, 59)
        self.set_fill_color(240, 249, 255)  # Very light blue
        self.set_draw_color(37, 99, 235)  # Cobalt Blue
        self.set_line_width(0.5)
        
        # Dry run to find height
        height_pdf = FPDF(unit="mm")
        height_pdf.add_page()
        height_pdf.set_font("helvetica", "I", 9.5)
        height_pdf.set_margins(20, 20, 20)
        lines = height_pdf.multi_cell(166, 5, text, split_only=True)
        h = len(lines) * 5 + 6
        
        # Draw box and text
        self.rect(x, y, 170, h, 'FD')
        self.set_xy(x + 4, y + 3)
        self.multi_cell(162, 5, text)
        self.set_xy(x, y + h + 2)
        self.ln(2)

def generate_pdf():
    pdf = HireviumWhitepaper(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    
    # ----------------------------------------------------
    # COVER PAGE
    # ----------------------------------------------------
    pdf.add_page()
    
    # Large colored accent blocks on the left margin
    pdf.set_fill_color(37, 99, 235)  # Cobalt Blue
    pdf.rect(0, 0, 12, 297, 'F')
    pdf.set_fill_color(6, 182, 212)  # Cyber Teal
    pdf.rect(12, 0, 4, 297, 'F')
    
    pdf.set_left_margin(30)
    pdf.set_right_margin(20)
    
    pdf.ln(45)
    pdf.set_font("helvetica", "B", 34)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 12, "HIREVIUM", new_x="LMARGIN", new_y="NEXT", align="L")
    
    pdf.set_font("helvetica", "B", 16)
    pdf.set_text_color(6, 182, 212)  # Cyber Teal
    pdf.cell(0, 8, "The AI Hiring Intelligence Operating System", new_x="LMARGIN", new_y="NEXT", align="L")
    
    pdf.ln(12)
    pdf.set_draw_color(226, 232, 240)
    pdf.set_line_width(0.8)
    pdf.line(30, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(15)
    
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(0, 6, "A groundbreaking, high-fidelity platform that redefines technical candidate evaluation. Combining real-time Adaptive Skill Verification, Multi-Persona AI War Room panel consensus, and digital twin analytics, HIREVIUM eliminates hiring friction, resume padding, and reviewer fatigue.")
    
    pdf.ln(60)
    
    # Submission Info Card (bordered box)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(37, 99, 235)
    pdf.set_line_width(0.3)
    pdf.rect(x, y, 160, 42, 'FD')
    
    pdf.set_xy(x + 5, y + 4)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 6, "HACKATHON SUBMISSION DETAILS", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(40, 5, "Project Repository:", new_x="RIGHT", new_y="TOP")
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "github.com/Adityasri05/Hirevium", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(40, 5, "Live Application Link:", new_x="RIGHT", new_y="TOP")
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "hirevium-production.up.railway.app", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(40, 5, "Developer Portfolio:", new_x="RIGHT", new_y="TOP")
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5, "Adityasri05", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(40, 5, "Submission Date:", new_x="RIGHT", new_y="TOP")
    pdf.set_font("helvetica", "B", 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5, "June 2026", new_x="LMARGIN", new_y="NEXT")
    
    # ----------------------------------------------------
    # SECTION 1: EXECUTIVE SUMMARY & ELEVATOR PITCH
    # ----------------------------------------------------
    pdf.add_page()
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    pdf.set_xy(20, 20)
    
    pdf.section_header("1. Executive Summary & Pitch")
    pdf.p("In today's fast-paced technology ecosystem, hiring qualified engineering talent has become one of the most expensive and error-prone challenges that companies face. Recruitment is plagued by widespread resume padding, superficial coding bootcamps, automated screening filters that eliminate strong atypical candidates, and severe engineering interviewer fatigue. Interviewers spend countless hours conducting basic filtering loops, only to find candidates lack core analytical skills. HIREVIUM completely reinvents this cycle.")
    
    pdf.p("HIREVIUM is a state-of-the-art AI Hiring Intelligence Operating System that replaces static resume sorting and standardized, easily-cheated coding challenges with a dynamic, high-fidelity hiring workspace. It integrates deep natural language processing and multimodal AI models to perform a complete evaluation of a candidate from initial upload to final panel consensus.")
    
    pdf.draw_callout("Elevator Pitch: HIREVIUM transforms hiring from a guessing game into an exact intelligence operation. By combining real-time Adaptive Skill Verification (which escalates or de-escalates difficulty based on candidate response performance) with an AI Hiring War Room committee panel simulating Engineering Directors and recruiters, HIREVIUM produces a multi-dimensional digital candidate twin profile. It evaluates technical accuracy, learning velocity, and project risks, resulting in a single, verified Hiring Readiness Score.")
    
    pdf.p("Designed to operate as a standalone SaaS workspace or integrate into existing Application Tracking Systems (ATS), HIREVIUM delivers candidate insights that traditional platforms miss. In doing so, it saves up to 80% of human engineering review time while boosting hiring quality and candidate satisfaction.")

    # ----------------------------------------------------
    # SECTION 2: THE PROBLEM STATEMENT
    # ----------------------------------------------------
    pdf.section_header("2. The Problem Statement")
    pdf.p("The traditional hiring pipeline is broken at multiple intersections. Recruiters, engineering managers, and candidates all suffer from structural inefficiencies that delay onboarding and result in costly mis-hires. We categorize these bottlenecks into four primary problems:")
    
    pdf.bullet("Resume Padding and Deceptive Profiles", "With the rise of generative AI, candidates can now easily create hyper-optimized resumes that match any job description perfectly on paper. Reviewing static resumes manually is no longer a reliable indicator of actual skill, forcing teams to rely on expensive and stressful technical rounds to uncover baseline capabilities.")
    
    pdf.bullet("Superficial and Out-of-Context Coding Tests", "Platforms like LeetCode or HackerRank encourage rote memorization of algorithms rather than practical engineering. Candidates can easily cheat using online assistants, and these platforms fail to test system design, communication skills, and real-world debugging.")
    
    pdf.bullet("High Engineering Cost & Interviewer Fatigue", "Conducting live coding loops eats up valuable engineering hours. Senior developers spend significant working time grading basic technical tests and conducting screens instead of writing code and shipping core features.")
    
    pdf.bullet("Lack of Structured, Multidisciplinary Consensus", "A typical hiring decision is based on unstructured notes from different interviewers, leading to personal bias, inconsistent evaluation criteria, and delayed decision-making cycles.")

    # ----------------------------------------------------
    # SECTION 3: THE HIREVIUM SOLUTION
    # ----------------------------------------------------
    pdf.add_page()
    pdf.section_header("3. The HIREVIUM Solution")
    pdf.p("HIREVIUM approaches engineering recruitment not as a series of disconnected questionnaires, but as a unified, data-driven intelligence pipeline. It uses advanced agents to guide the candidate and the recruiter through a seamless verification cycle:")
    
    # Grid of core pipeline stages
    x = pdf.get_x()
    y = pdf.get_y()
    
    # Column 1
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(226, 232, 240)
    pdf.rect(x, y, 80, 42, 'FD')
    pdf.set_xy(x + 3, y + 3)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "1. Resume Parsing", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(74, 4, "High-fidelity resume upload and entity extraction. Identifies claimed skills, experience duration, and projects, feeding them into the candidate database.")
    
    # Column 2
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(x + 90, y, 80, 42, 'FD')
    pdf.set_xy(x + 93, y + 3)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "2. JD Intelligence", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(74, 4, "Extracts core requirements, tech stacks, and soft-skill needs from job descriptions, defining a custom evaluation baseline for the role.")
    
    pdf.ln(12)
    y2 = pdf.get_y()
    # Row 2 Column 1
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(x, y2, 80, 42, 'FD')
    pdf.set_xy(x + 3, y2 + 3)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "3. Adaptive Interviewing", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(74, 4, "Conducts dynamic, context-aware Q&A. The AI shifts difficulty in real time based on candidate answers to establish a true threshold.")
    
    # Row 2 Column 2
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(x + 90, y2, 80, 42, 'FD')
    pdf.set_xy(x + 93, y2 + 3)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "4. AI Hiring War Room", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(74, 4, "Four distinct AI expert agents debate the candidate's answers, generating individual verdicts and consensus scores, identifying hiring risks.")
    
    pdf.set_xy(x, y2 + 45)
    pdf.ln(3)
    
    pdf.p("By transitioning away from static templates, Hirevium captures rich qualitative signals like communication clarity under pressure, problem-solving structure, and learning velocity. It maps these parameters into a Digital Candidate Twin profile, which lets recruiters visualize how the candidate fits within the target team's requirements.")

    # ----------------------------------------------------
    # SECTION 4: DEEP DIVE: ARCHITECTURE & INNOVATIONS
    # ----------------------------------------------------
    pdf.section_header("4. Deep Dive: Key Innovations")
    
    pdf.subsection_header("A. The Adaptive Interview Engine")
    pdf.p("At the core of HIREVIUM is the Adaptive Interview Engine. Traditional technical screens follow a linear structure that is either too easy or too hard, failing to pinpoint a candidate's true capability boundary. Hirevium dynamically adjusts the interview trajectory based on response evaluation:")
    
    pdf.bullet("Difficulty Escalation (Score >= 85%)", "If a candidate provides an expert answer, the engine flags their performance and raises the difficulty. It asks deep, architectural follow-up questions to test theoretical limits and edge-case handling.")
    pdf.bullet("Sideways Pivot (Score 60% - 84%)", "If the candidate shows baseline competency, the engine keeps the difficulty level stable but pivots to a parallel concept (e.g., switching from react hooks to component lifecycle) to test breadth of knowledge.")
    pdf.bullet("De-escalation (Score < 60%)", "If the candidate struggles, the engine gently de-escalates to fundamental concepts, ensuring they aren't completely blocked while establishing their exact baseline threshold.")
    
    pdf.subsection_header("B. The AI Hiring War Room Committee Panel")
    pdf.p("Once the adaptive interview completes, the entire session transcript, along with resume and job description contexts, is submitted to the AI Hiring War Room. This module simulates a complete technical hiring committee consisting of four distinct AI personas:")
    
    pdf.bullet("Technical Lead", "Focuses strictly on code accuracy, architectural design choices, optimization techniques, security best practices, and edge cases.")
    pdf.bullet("Engineering Manager", "Evaluates teamwork, project execution methodologies, SDLC understanding, agile practices, and mentoring capabilities.")
    pdf.bullet("Recruiter", "Analyzes salary expectations, career alignment, location fit, onboarding timelines, and cultural add.")
    pdf.bullet("VP of Engineering", "Reviews overall ROI, strategic team placement, long-term leadership potential, and critical organizational risks.")
    
    pdf.p("These four agents debate the candidate's responses, returning structured scores, positive findings, concerns, and final recommendations. This consensus model significantly reduces individual bias and produces a unified hiring recommendation.")

    # ----------------------------------------------------
    # SECTION 5: TECHNICAL STACK & ARCHITECTURE
    # ----------------------------------------------------
    pdf.add_page()
    pdf.section_header("5. Technical Stack & Architecture")
    pdf.p("HIREVIUM is engineered as a decoupled, responsive web application utilizing a fast asynchronous backend and a premium Next.js frontend. The architecture is designed to handle real-time streaming, complex agent orchestration, and secure authentication.")
    
    # Tech stack table
    pdf.set_font("helvetica", "B", 10)
    pdf.set_fill_color(37, 99, 235)  # Cobalt Blue
    pdf.set_text_color(255, 255, 255)
    
    # Headers
    pdf.cell(50, 8, "Layer", border=1, new_x="RIGHT", new_y="TOP", align="C", fill=True)
    pdf.cell(60, 8, "Technology", border=1, new_x="RIGHT", new_y="TOP", align="C", fill=True)
    pdf.cell(60, 8, "Role", border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
    
    # Rows
    rows = [
        ("Frontend UI", "Next.js 16 (React 19), TypeScript", "Component routing, dashboard UI, auth integrations"),
        ("Styling System", "Tailwind CSS v4 (Global CSS tokens)", "Responsive, unified Cobalt & Cyber Teal themes"),
        ("Animation Library", "Framer Motion", "Micro-animations, smooth layouts, drawer transitions"),
        ("Backend APIs", "FastAPI, Python (Uvicorn)", "Asynchronous endpoints, JSON routers, file uploads"),
        ("AI Agents Framework", "Google Gemini Pro (API Key / Fallback)", "Adaptive interview generation, War Room orchestration"),
        ("Database Layer", "SQLite, SQLAlchemy (AioSQLite)", "Asynchronous ORM, candidate & interview session storage"),
        ("Authentication & DB", "Supabase & Firebase SDKs", "Secure signup, JWT generation, session syncing"),
    ]
    
    pdf.set_font("helvetica", "", 8.5)
    pdf.set_text_color(51, 65, 85)
    
    alternate = False
    for layer, tech, role in rows:
        if alternate:
            pdf.set_fill_color(248, 250, 252)
        else:
            pdf.set_fill_color(255, 255, 255)
            
        pdf.cell(50, 7, layer, border=1, new_x="RIGHT", new_y="TOP", align="L", fill=True)
        pdf.cell(60, 7, tech, border=1, new_x="RIGHT", new_y="TOP", align="L", fill=True)
        pdf.cell(60, 7, role, border=1, new_x="LMARGIN", new_y="NEXT", align="L", fill=True)
        alternate = not alternate
        
    pdf.ln(4)
    
    pdf.subsection_header("Agent Orchestration and Fallback System")
    pdf.p("To maintain 100% service uptime even when Gemini API keys are rate-limited or quota is exhausted (which is highly common on free tiers), Hirevium implements an elegant Asynchronous Agent Fallback Controller. When the API returns a 429 or network exception, the system dynamically switches to an offline heuristics parser:")
    
    pdf.bullet("Contextual Heuristics Engine", "Analyzes the semantic category of the candidate's response (e.g. databases, state management, algorithmic complexity, UI rendering).")
    pdf.bullet("Dynamic Response Templates", "Retrieves rich structured grading criteria, comments, and appropriate follow-up questions from a localized JSON database.")
    pdf.bullet("Disclosure Integrity", "Appends a clean disclosure badge to indicate the system is running in offline validation, maintaining auditability without disrupting the candidate's interview flow.")

    # ----------------------------------------------------
    # SECTION 6: COMPETITIVE ANALYSIS & USPs
    # ----------------------------------------------------
    pdf.section_header("6. Competitive Analysis & USPs")
    pdf.p("Existing technical screening tools fail to capture the multi-dimensional complexity of actual developer work. HIREVIUM offers significant advantages over industry incumbents:")
    
    # Comparison table
    pdf.set_font("helvetica", "B", 9.5)
    pdf.set_fill_color(37, 99, 235)
    pdf.set_text_color(255, 255, 255)
    
    # Headers
    pdf.cell(45, 8, "Feature", border=1, new_x="RIGHT", new_y="TOP", align="C", fill=True)
    pdf.cell(42, 8, "Traditional Platforms", border=1, new_x="RIGHT", new_y="TOP", align="C", fill=True)
    pdf.cell(42, 8, "AI Chatbots (Generic)", border=1, new_x="RIGHT", new_y="TOP", align="C", fill=True)
    pdf.cell(41, 8, "HIREVIUM OS", border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
    
    pdf.set_font("helvetica", "", 8)
    pdf.set_text_color(51, 65, 85)
    
    comp_rows = [
        ("Adaptive Difficulty", "None (Static Q&A templates)", "Basic follow-up prompts", "Real-time, score-based pivots"),
        ("Multi-Agent Verdicts", "None (Manual scorecard)", "Single-prompt analysis", "4 distinct AI panels with debate"),
        ("Cheating Resistance", "Plagiarism checks only", "None (Easily copy-pasted)", "Adaptive context verification Qs"),
        ("Analytics", "Simple score / duration", "Raw text summaries", "Digital Twin, Velocity, Risk badge"),
        ("ATS Integration", "Yes (API integrations)", "None (Standalone)", "Native ATS API design & SPA widgets"),
    ]
    
    alternate = False
    for feat, trad, chat, hire in comp_rows:
        if alternate:
            pdf.set_fill_color(248, 250, 252)
        else:
            pdf.set_fill_color(255, 255, 255)
            
        pdf.cell(45, 7, feat, border=1, new_x="RIGHT", new_y="TOP", align="L", fill=True)
        pdf.cell(42, 7, trad, border=1, new_x="RIGHT", new_y="TOP", align="L", fill=True)
        pdf.cell(42, 7, chat, border=1, new_x="RIGHT", new_y="TOP", align="L", fill=True)
        
        # Highlight HIREVIUM column in cyan/blue text or bold
        pdf.set_font("helvetica", "B", 8)
        pdf.set_text_color(37, 99, 235)
        pdf.cell(41, 7, hire, border=1, new_x="LMARGIN", new_y="NEXT", align="L", fill=True)
        
        pdf.set_font("helvetica", "", 8)
        pdf.set_text_color(51, 65, 85)
        alternate = not alternate

    # ----------------------------------------------------
    # SECTION 7: BUSINESS & MONETIZATION
    # ----------------------------------------------------
    pdf.add_page()
    pdf.section_header("7. Business Model & ROI")
    pdf.p("HIREVIUM's go-to-market and monetization strategy focuses on B2B SaaS licensing, targeting mid-sized to enterprise technology organizations. We implement three core revenue streams:")
    
    pdf.bullet("Recruiter Seat Licensing", "A tier priced at $79 per seat/month. Designed for standard recruiters, enabling unlimited resume parses, JD evaluations, and up to 50 active candidate interviews per month.")
    
    pdf.bullet("Enterprise Pay-Per-Candidate", "Custom corporate tiers ($299/month + usage fees). Offers unlimited active interviews, complete customizable AI panel personas (e.g. adapting the EM panel to match company-specific cultural values), and automated calendar integrations.")
    
    pdf.bullet("ATS Integration Add-On", "Premium plug-in subscriptions for popular platforms like Greenhouse, Lever, and Workday. Automatically syncs Digital Twin scores and candidate transcripts directly into the company's existing ATS UI.")
    
    pdf.subsection_header("ROI Analysis for Enterprises")
    pdf.p("To prove enterprise value, we run a simple ROI calculation based on engineering hours saved:")
    pdf.draw_callout("Typical Technical Hiring Screen Cost:\n- Time spent per resume review and initial screen: 1.5 engineering hours ($150 value)\n- For 200 candidates per role = 300 engineering hours = $30,000 cost.\n\nHIREVIUM Cost and Savings:\n- Automated Adaptive Screening conducts the initial screens, filtering the pool to the top 10% (20 candidates).\n- Engineers only conduct live loops for the top 20 candidates = 30 engineering hours.\n- Net Savings: 270 engineering hours ($27,000 saved per open role!).")

    # ----------------------------------------------------
    # SECTION 8: FUTURE ROADMAP & SCALING
    # ----------------------------------------------------
    pdf.section_header("8. Future Roadmap & Scaling")
    pdf.p("As we continue to develop the HIREVIUM system, we have mapped out a detailed 3-phase technical roadmap to expand our capabilities and integrate more deeply into the developer hiring cycle:")
    
    pdf.subsection_header("Phase 1: Real-time Audio Streaming (Q3 2026)")
    pdf.p("Upgrade the text-based adaptive interview to support low-latency real-time voice conversations. Using WebRTC and streaming speech-to-text / text-to-speech models, candidates will speak their answers directly. This enables checking verbal communication clarity, conversational flow, and articulation under pressure in real time.")
    
    pdf.subsection_header("Phase 2: Headless IDE and Multi-File Debugging (Q4 2026)")
    pdf.p("Introduce a full visual workspace containing a sandboxed web IDE. Rather than simple algorithm questions, candidates will be presented with a multi-file buggy codebase (matching the job description's actual stack) and asked to debug or add a feature. The AI engine will track cursor movements, lint errors, keystrokes, and debugging methodology.")
    
    pdf.subsection_header("Phase 3: ATS Automated Orchestration (Q2 2027)")
    pdf.p("Integrate fully with background check APIs, automated calendar schedulers, and direct ATS push systems. The platform will operate autonomously: trigger an interview on candidate application, compile the War Room verdict, run the verification checks, and push the top candidates directly to the manager's interview schedule.")

    # ----------------------------------------------------
    # SECTION 9: CONCLUSION & TEAM
    # ----------------------------------------------------
    pdf.section_header("9. Conclusion")
    pdf.p("HIREVIUM is not just another recruitment tool; it is a fundamental shifting of the balance of technical hiring. By automating early filtering, eliminating padding deception through adaptive Q&A, and providing recruiters with multi-persona engineering intelligence, HIREVIUM returns critical working hours back to development teams while ensuring that companies hire the absolute best talent.")
    
    pdf.p("We are excited to submit HIREVIUM to the Hackathon, demonstrating a fully functional, premium UI-styled, production-ready implementation that solves a major problem in our industry.")
    
    pdf.ln(10)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(37, 99, 235)
    pdf.cell(0, 5, "Submitted by Team Hirevium", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("helvetica", "I", 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, "Codebase, Deployment, and Assets available at github.com/Adityasri05/Hirevium", new_x="LMARGIN", new_y="NEXT", align="C")

    # Output file
    output_filename = r"d:\Hackathon Projects\HireIQ\Hirevium_Hackathon_Submission.pdf"
    pdf.output(output_filename)
    print(f"PDF successfully generated at: {output_filename}")

if __name__ == "__main__":
    generate_pdf()
