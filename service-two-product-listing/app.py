import pytest
import http_port as http

testResult = pytest.main()

if(testResult == 0):
    print("\nAll tests passed")
    print("Starting server...\n")
    http.startServer()
else:
    raise Exception("Tests failed")
    