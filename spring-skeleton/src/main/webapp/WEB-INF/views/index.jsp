<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<a
		href="https://kauth.kakao.com/oauth/authorize?client_id=caca7722fcbd20626b2343a0f5bf4083&redirect_uri=http://localhost:8080/login&response_type=code">
		<img src="/img/kakao.png">
	</a>
	<br>
	<h3>${access_Token}</h3>
	<input type="button" value="로그아웃" onclick="location.href='/logout/?access_Token=${access_Token}'">
</body>

</html>
