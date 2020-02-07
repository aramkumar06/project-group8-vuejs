package com.ssafy.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.UserService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class UserRestController {
	@Autowired
	private UserService userService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("회원 등록")
	@PostMapping("/user/insert/{userID}_{userName}_{userEmail}")
	public ResponseEntity<Map<String, Object>> insertUser(@PathVariable String userID, @PathVariable String userName, @PathVariable String userEmail){
		User user = new User();
		user.setUserID(userID);
		user.setUserName(userName);
		user.setUserEmail(userEmail);
		userService.insertUser(user); 
		return handleSuccess("회원 등록 성공");
	}
	
	@ApiOperation("userID로 회원정보 조회")
	@GetMapping("/user/{userID}")
	public ResponseEntity<Map<String, Object>> search(@PathVariable String userID){
		User user = userService.search(userID); 
		return handleSuccess(user);
	}
	
	@ApiOperation("userID로 사용자가 즐겨찾기 한 유투버 정보 검색")
	@GetMapping("/user/favorite/{userID}")
	public ResponseEntity<Map<String, Object>> searchUserFavoriteYoutuber(@PathVariable String userID){
		List<Youtuber> list = userService.searchUserFavoriteYoutuber(userID); 
		return handleSuccess(list);
	}

	@ApiOperation("userID로 회원 가입 여부 조회")
	@GetMapping("/user/exist/{userID}")
	public ResponseEntity<Map<String, Object>> searchUserExist(@PathVariable String userID){
		int userCount = userService.searchUserExist(userID); 
		return handleSuccess(userCount);
	}
	
	// Exception Handle
	public ResponseEntity<Map<String, Object>> handleFail(Object data, HttpStatus state){
		Map<String, Object> resultMap = new HashMap<String, Object>();
		resultMap.put("state", "fail");
		resultMap.put("data", data);
		return new ResponseEntity<Map<String,Object>>(resultMap, state);
	}
	public ResponseEntity<Map<String, Object>> handleSuccess(Object data){
		Map<String, Object> resultMap = new HashMap<String, Object>();
		resultMap.put("state", "ok");
		resultMap.put("data", data);
		return new ResponseEntity<Map<String,Object>>(resultMap, HttpStatus.OK);
	}	
}