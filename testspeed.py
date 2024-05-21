import speedtest
speed = speedtest.Speedtest()
dowload_speed = speed.download()
upload_speed = speed.upload()
print(f'The download speed is {dowload_speed}')
print(f'The upload speed is {upload_speed}')
