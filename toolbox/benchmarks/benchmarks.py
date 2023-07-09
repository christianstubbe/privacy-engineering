import subprocess
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('../src/creds.json')


def run_ab(benchmark_url, number_of_requests, concurrency_level):
    ab_command = f"ab -n {number_of_requests} -c {concurrency_level} {benchmark_url}"
    try:
        process = subprocess.run(ab_command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while trying to run `ab` command: {e}")
        return None
    output = process.stdout

    return output


output = run_ab("http://localhost:8000", 1000, 10)
if output:
    print(output)
