from core import Module
from perennial_portal import PerennialPortal
from rituals import RitualScheduler
from calendar import AstroCalendar
from projections import TemporalVisualizations
from surveys import InsightsSurvey

class CyclesOfTimeModule(Module):
    def __init__(self):
        self.portal = PerennialPortal()
        self.rituals = RitualScheduler()
        self.calendar = AstroCalendar()
        self.projections = TemporalVisualizations()
        self.survey = InsightsSurvey()

    async def explore_temporal_concepts(self):
        concept = await self.portal.choose_temporal_concept()
        lesson = await self.portal.get_lesson(concept)

    async def attune_to_cosmic_rhythms(self):
        ritual = await self.rituals.schedule_by_calendar(self.calendar)

    async def visualize_timely_forces(self):
        concept = await self.portal.choose_temporal_concept()
        projection = await self.projections.play_concept(concept)

    async def gather_cycle_insights(self):
        responses = await self.survey.conduct()

    async def access_aggregated_insights(self):
        # Allow users to access aggregated perspectives and common themes on a concept's influence
        insights = await self.portal.get_aggregated_insights()
        await self.portal.display_insights(insights)

    async def grant_license_for_artistic_creations(self):
        # Offer a license for users to create artistic works inspired by projections
        await self.portal.grant_license_for_artistic_creations()
