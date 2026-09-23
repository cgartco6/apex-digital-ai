from crewai import Crew, Process
from design_studio.crew import create_design_crew
from branding_studio.crew import create_branding_crew
from web_dev_studio.crew import create_webdev_crew
from marketing_studio.crew import create_marketing_crew

class ApexOrchestrator:
    def __init__(self):
        self.design = create_design_crew()
        self.branding = create_branding_crew()
        self.web = create_webdev_crew()
        self.marketing = create_marketing_crew()

    def run_full_project(self, brief):
        design = self.design.kickoff(inputs={"brief": brief})
        branding = self.branding.kickoff(inputs={"brief": brief})
        web = self.web.kickoff(inputs={"brief": brief})
        marketing = self.marketing.kickoff(inputs={"brief": brief})
        return "All studios completed successfully."
