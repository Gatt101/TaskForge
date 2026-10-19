from .schemas import JobResponse

class JobRepository:
    def __init__(self):
        self.jobs:dict [int,JobResponse] = {}
        self.next_id:int = 1
        
    def generate_id(self) -> int:
        job_id = self.next_id
        self.next_id += 1
        return job_id
    
    def create(self, job: JobResponse) -> JobResponse:
        self.jobs[job.id] = job
        return job
    
    def get_all(self) -> list[JobResponse]:
        return list(self.jobs.values())
    
    def get(self, job_id: int) -> JobResponse | None:
        return self.jobs.get(job_id)
    
    def update(self, job_id: int, changes : dict) -> JobResponse | None:
        job = self.jobs.get(job_id)
        
        if job is None:
            return None
        
        updated_job = job.model_copy(update=changes)
        self.jobs[job_id] = updated_job
        return updated_job
    
    def delete(self, job_id: int) -> bool:
        if job_id not in self.jobs:
            return False
        
        del self.jobs[job_id]
        return True
        