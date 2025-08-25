from fastapi import FastAPI, Request, Response
from lxml import etree
from app.responses import (
    soap_fault_invalid_format,
    soap_fault_meter_info,
    soap_success_response,
    soap_not_found_response,
)

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "Meter Confirmation Service",
        "status": "running",
        "docs": "/docs",
        "example": "/confirm-meter/12345"
    }

@app.post("/meter/confirm/")
async def confirm_meter(request: Request):
    try:
        body = await request.body()
        if not body:
            return Response(content=soap_fault_invalid_format(), media_type="text/xml")

        root = etree.fromstring(body)

        # Find the meterIdentifier element regardless of prefix, as long as it uses the base schema namespace.
        meter_elem = root.find(".//{http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema}meterIdentifier")
        if meter_elem is None:
            return Response(content=soap_fault_invalid_format(), media_type="text/xml")

        msno = meter_elem.get("msno")
        if not msno:
            return Response(content=soap_fault_invalid_format(), media_type="text/xml")

        # Routing logic
        if msno == "01234567891":
            return Response(content=soap_fault_meter_info(), media_type="text/xml")
        elif msno == "01234567892":
            return Response(content=soap_not_found_response(), media_type="text/xml")
        elif msno == "01234567890" or (msno.isdigit() and len(msno) == 11):
            return Response(content=soap_success_response(msno), media_type="text/xml")
        else:
            return Response(content=soap_fault_invalid_format(), media_type="text/xml")

    except Exception:
        # Any parsing error or unexpected issue → invalid format fault
        return Response(content=soap_fault_invalid_format(), media_type="text/xml")

