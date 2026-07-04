# TechDoc AI Development Journey

## Day 1

### Learned
- FastAPI basics
- API concepts
- GET and POST
- Class vs Object

### Built
- Project structure
- First FastAPI app

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Day 2

### Learned
- JSON
- Uvicorn server
- localhost and ports
- Swagger documentation
- Git workflow

### Built
- Running backend API
- GitHub repository setup

### Problems Faced
- PowerShell execution policy issue
- Accidentally staged venv folder

### Solutions
- Activated venv correctly
- Used .gitignore and git reset

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Day 3

### Learned
- FastAPI file upload endpoint
- UploadFile and File classes
- multipart/form-data request type
- File storage in backend
- Binary file handling
- File paths and folders
- shutil.copyfileobj()
- Why file buffers are used
- Updating .gitignore correctly

### Built
- PDF upload API (/upload)
- Storage folder for uploaded PDFs
- Save uploaded PDF to disk
- Return filename, content type and storage path in JSON response

### Problems Faced
- FastAPI required python-multipart package
- Upload endpoint failed because dependency was missing
- Git commands were executed inside the backend folder instead of project root
- Storage files started appearing in Git

### Solutions
- Installed python-multipart
- Restarted the FastAPI server
- Executed Git commands from the project root
- Added storage files to .gitignore
- Used git rm --cached to stop tracking uploaded PDFs

### Key Concepts
- UploadFile
- File(...)
- multipart/form-data
- Binary data
- File buffer
- shutil.copyfileobj()
- Storage directory
- .gitignore

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------