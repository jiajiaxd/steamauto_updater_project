addEventListener('fetch', event => {
	event.respondWith(handleRequest(event.request))
  })
  
  async function handleRequest(request) {
	const url = new URL(request.url)
  
	// 检查路径是否为 /versions
	if (url.pathname === '/versions') {
	  // 构建 GitHub RAW 文件的 URL
	  const githubUrl = 'https://github.com/jiajiaxd/Steamauto/raw/master/versions.json'
  
	  // 发起 HTTP 请求
	  const response = await fetch(githubUrl)
  
	  // 返回 GitHub RAW 文件的内容
	  return new Response(await response.text(), {
		status: response.status,
		headers: {
		  'Content-Type': 'application/json;charset=UTF-8',
		  'Access-Control-Allow-Origin': '*'
		}
	  })
	}
  
	// 如果路径不是 /versions，继续请求其他资源
	return new Response(JSON.stringify({
		'error': '404 Not Found'
	}))
  }
  