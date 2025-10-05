import os
def run_file_operation():
    filename="text.txt"
    test_content="Hello from the CI pipeline"
    
    try: 
        print("Starting the application")
        print(f"Writing to {filename}")
        with open(filename, 'w') as f:
            f.write(test_content)
            
        print(f"Reading the {filename}")
        with open(filename,'r') as f:
            content = f.read()
            
        assert content == test_content,"Verification failed: Content does not match"
        
        print("Content Verification successful")
        print("Application finished successfully")
        
        
    except Exception as e:
        print("Application Failed")
        exit(1)
        
    finally:
        if os.path.exists(filename):
            print(f"cleaning up {filename}")
            os.remove(filename)

if __name__ == "__main__":
    run_file_operation()
        