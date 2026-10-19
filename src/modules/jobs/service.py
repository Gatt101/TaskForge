from datetime import datetime , timezone
from fastapi  import HTTPException, status

from .schemas import JobCreate, JobUpdate, JobResponse, JobStatus
from .repository import JobRepository

class JobService:
    def __init__(self, repository: JobRepository):
        self.repository = repository
        
    def create_job(self,data: JobCreate) -> JobResponse:
        job = JobResponse(
            id= self.repository.generate_id(),
            title=data.title,
            description=data.description,
            status=JobStatus.PENDING,
            created_at=datetime.now(timezone.utc),
        )
        
        return self.repository.create(job)
    
    def list_jobs(self, job_status:JobStatus | None = None) -> list[JobResponse]:
        jobs = self.repository.get_all()
        
        if job_status:
            jobs = [job for job in jobs if job.status == job_status]
        
        return jobs
    
    def get_job(self, job_id: int) -> JobResponse:
        job = self.repository.get(job_id)

        if job is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )

        return job

    def update_job(
        self, job_id: int, data: JobUpdate
    ) -> JobResponse:
        self.get_job(job_id)

        changes = data.model_dump(exclude_unset=True)

        updated_job = self.repository.update(job_id, changes)

        if updated_job is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )

        return updated_job

    def delete_job(self, job_id: int) -> None:
        deleted = self.repository.delete(job_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found",
            )
