# TivixQA
After cloning go to repository dir.
make results dir.
To build image type: docker build --no-cache --rm -f "Dockerfile" -t tivixqa:latest .
To run tests type: docker run -it --mount type=bind,source=RESULT_PATH,target=/results tivixqa:latest pytest /tests/test_careers_page.py --alluredir /results
To generate allure report type: docker run -it --rm --mount type=bind,source=RESULTS_PATH,target=/output -w /output beeete2/docker-allure2 allure generate /output -o /output/reports/ --clean
Ten go to your results path -> report -> index.html