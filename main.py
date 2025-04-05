from fastapi import FastAPI, Request, Header
from typing import Optional, Dict
import json


app = FastAPI()

@app.post("/api/pms/v1/events")
async def get_events(request: Request, body_data:Dict, authorization:Optional[str] = Header(None)):
    """
    # 참고: FastAPI는 JSON 본문을 자동으로 파이썬 딕셔너리로 변환하여 엔드포인트 함수의 인자로 제공합니다.
    """
    # client IP address 출력
    print(f"Received request from: {request.client.host}")

    # request method 출력
    print(f"Request method: {request.method}")
   
    # request url 출력
    print(f"Request endpoint: {request.url.path}")

    # request headers 출력
    print(f"Authorization Token: {authorization}")

    # request body
    """
    참고: FastAPI는 JSON 본문을 자동으로 파이썬 딕셔너리로 변환하여 엔드포인트 함수의 인자로 제공합니다.
    원본 본문(raw body)을 가져오려면 request.body() 메서드를 사용할 수 있습니다.
    하지만, 파싱된 JSON 데이터를 가져오려면 request.json() 메서드를 사용하면 되고, 
    이 경우 딕셔너리 형태로 반환됩니다.
    """
    
    # data = await request.json() 
    
    print(f"Received body:")

    # JSON 데이터를 보기 좋게 출력
    """
    # 참고: json.dumps()는 파이썬 객체를 JSON 문자열로 변환하는 데 사용됩니다.
    # indent 매개변수를 사용하여 JSON 문자열을 보기 좋게 정렬할 수 있습니다.
    # ensure_ascii 매개변수를 False로 설정하면, ASCII 문자가 아닌 문자(예: 한글)도 올바르게 출력됩니다.
    """
    print(json.dumps(body_data, indent=4, ensure_ascii=False))

    # status code 는?
    """
    FastAPI는 기본적으로 200 OK 상태 코드를 반환합니다.
    다른 상태 코드를 반환하려면, FastAPI의 Response 객체를 사용하거나,
    JSONResponse 객체를 사용하여 원하는 상태 코드를 설정할 수 있습니다.
    예를 들어, 201 Created 상태 코드를 반환하려면 다음과 같이 작성할 수 있습니다.
    from fastapi.responses import JSONResponse
    return JSONResponse(content={"message": "success"}, status_code=201)
    또는, FastAPI의 Response 객체를 사용하여 다음과 같이 작성할 수 있습니다.
    from fastapi import Response
    return Response(content=json.dumps({"message": "success"}), media_type="application/json", status_code=201)
    FastAPI는 기본적으로 JSON 응답을 반환합니다.
    """
    return {"message": "success"}

