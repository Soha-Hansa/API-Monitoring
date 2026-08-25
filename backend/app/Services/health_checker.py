import httpx
import time


def check_api(url):
    start = time.perf_counter()

    try:
        response = httpx.get(url, timeout=5)

        end = time.perf_counter()
        latency = end - start
        status_code = response.status_code
        is_success = 200 <= status_code < 300

        return {
            "status_code": status_code,
            "latency": latency,
            "is_success": is_success
        }

    except (httpx.ConnectError, httpx.TimeoutException):

        end = time.perf_counter()
        latency = end - start

        return {
            "status_code": None,
            "latency": latency,
            "is_success": False
        }