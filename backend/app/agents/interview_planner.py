from app.agents.base_agent import call_gemini

SYSTEM_PROMPT = """You are the Interview Planner Agent for HireIQ. You create interview blueprints.

Based on the candidate's resume and the job description, plan an adaptive interview.

Question distribution:
- 40% JD-specific skills
- 30% Resume project deep-dives
- 20% Fundamentals
- 10% Behavioral

Return a JSON object with EXACTLY this structure:
{
  "knowledge_graph": {
    "root": "Interview Topics",
    "nodes": [
      {
        "topic": "React",
        "subtopics": ["Hooks", "State Management", "Performance", "Testing"],
        "difficulty_range": "Medium-Hard",
        "weight": 0.3
      }
    ]
  },
  "question_plan": [
    {
      "order": 1,
      "topic": "React Hooks",
      "category": "technical",
      "difficulty": "Medium",
      "knowledge_node": "React > Hooks",
      "question_type": "concept|practical|scenario|behavioral"
    }
  ],
  "difficulty_progression": "Start Medium, escalate based on performance",
  "total_questions": 10,
  "estimated_duration_minutes": 30
}
"""


async def plan_interview(resume_data: dict, jd_data: dict, difficulty: str = "Medium") -> dict:
    """Create an interview plan based on resume and JD analysis."""
    user_prompt = f"""
Candidate Resume Analysis:
{resume_data}

Job Description Analysis:
{jd_data}

Starting Difficulty: {difficulty}

Create a comprehensive interview plan with a knowledge graph and question path.
"""
    return await call_gemini(SYSTEM_PROMPT, user_prompt)
