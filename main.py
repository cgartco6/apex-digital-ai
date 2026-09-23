import os
from dotenv import load_dotenv
from rich.console import Console
from orchestrator.orchestrator import ApexOrchestrator

load_dotenv()
console = Console()

def main():
    console.print("[bold green]🚀 Apex Digital AI Orchestrator[/bold green]")
    orchestrator = ApexOrchestrator()
    brief = input("\nEnter project brief: ") or "Build complete brand, website and marketing for AI SaaS product called NovaFlow."
    result = orchestrator.run_full_project(brief)
    console.print("[bold blue]✅ Project Complete[/bold blue]")

if __name__ == "__main__":
    main()
