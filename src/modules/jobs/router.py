
from fastapi import APIRouter, status

from .repository import JobRepository
from .schemas import JobCreate, JobUpdate, JobResponse, JobStatus
from .service import JobService


router = APIRouter(prefix="/jobs", tags=["Jobs"])

repository = JobRepository()
service = JobService(repository)


@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_job(data: JobCreate):
    return service.create_job(data)


@router.get("", response_model=list[JobResponse])
def list_jobs(status: JobStatus | None = None):
    return service.list_jobs(status)


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int):
    return service.get_job(job_id)


@router.patch("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, data: JobUpdate):
    return service.update_job(job_id, data)


@router.delete(
    "/{job_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_job(job_id: int):
    service.delete_job(job_id)
