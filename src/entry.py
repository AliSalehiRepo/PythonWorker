from js import Response

async def on_fetch(request):
    return Response.new("Hello from Python!")
