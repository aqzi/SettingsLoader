import datetime
from typing import Optional
from pydantic import BaseModel

class FeedingSchedule(BaseModel):
    food_type: str = "meat"
    feeding_times_per_day: int = 2

class MedicalHistory(BaseModel):
    primary_vet: str
    last_checkup_date: Optional[datetime.date] = None
    vaccinations_up_to_date: bool = False
    notes: Optional[str] = None

class CaretakerInfo(BaseModel):
    name: str
    contact_number: Optional[str] = None
    preferred_language: str = "English"
    area_of_expertise: str

class Characteristics(BaseModel):
    habitat: str
    lifespan_years: str

class Specs(BaseModel):
    weight_kg: float
    endangered: bool = False
    characteristics: Characteristics

class Preferences(BaseModel):
    favorite_toys: list[str]

class AnimalConfig(BaseModel):
    animal_name: str
    species: str
    specs: Specs
    feeding_schedule: FeedingSchedule
    medical_history: MedicalHistory
    caretaker_info: CaretakerInfo
    preferences: Preferences
    specs_copy: Specs
    specs_copy_with_overwrite: Specs