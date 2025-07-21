#DATA INGESTION : handling heterogeneous file formats

def validate_file(file):
    """Check if the uploaded file is an allowed type.
    
    Args: file: Uploaded file object with content_type attribute
    Returns: bool: True if file type is allowed, False otherwise
    
    """
    allowed_types = ["image/jpeg", "image/png", "text/plain", "application/pdf"]
    return file.content_type in allowed_types #checks if file type is allowed