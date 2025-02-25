import httpx

res = httpx.get('https://httpbin.org/get')
print(res.status_code)