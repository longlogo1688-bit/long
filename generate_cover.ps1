$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Bearer 9561c20ee48d541d7548a658842e4c40"
}

$body = @{
    model = "doubao-pro"
    prompt = "小红书封面图，左侧是中国三峡大坝发电站闪电标志，右侧是芯片电路图AI字样，中间大字写着'电出不了国，但Token可以'，对比强烈，科技感，红蓝配色，简洁大气，适合社交媒体封面，高对比度，文字清晰可读"
    size = "1024x1024"
    n = 1
    response_format = "url"
} | ConvertTo-Json

Invoke-WebRequest -Method Post -Uri "http://localhost:8000/v1/images/generations" -Headers $headers -Body $body -OutFile "cover_response.json"
