from fastapi import FastAPI, File, UploadFile 
from resume_parser import extract_text

# create a fastapi app instance 
app = FastAPI() 
# allows user to uploead a resume file
@app.post("/upload-resume/") 
# parameter accepts an uploaded file from the client_side form 
async def upload_resume(file: UploadFile = File(...)): 

    # extract the to isolate file extention pdf or docx and convert to .lower
    file_extention = os.path.splittext(file.filename)[1].lower()
    if file_extention not in [".pdf",".docx"]:
        return{"error": "Unsupported file format"}
    
    # temp file storage 
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # extracting text
    extracted_text = extract_text(file_path, file_extention)

    # file clean up 
    os.remove(file_path)

    # return reuslts 
    return {"file_name": file.filename, "content": extracted_text}

