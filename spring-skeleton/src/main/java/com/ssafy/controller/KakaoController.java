package com.ssafy.controller;

import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.ssafy.model.dto.User;
import com.ssafy.model.service.KakaoAPI;
import com.ssafy.model.service.UserService;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@Controller
public class KakaoController {
	
	@Autowired
    private KakaoAPI kakao;
	@Autowired
	private UserService userService;
	
	@RequestMapping(value="/")
    public String index() {
        
        return "index";
    }
	
	@RequestMapping(value="/login")
    public String login(@RequestParam("code") String code) {
        System.out.println("code:"+code);
    	String access_Token = kakao.getAccessToken(code);
    	HashMap<String, Object> userInfo = kakao.getUserInfo(access_Token);
    	System.out.println("login Controller : " + userInfo);
    	
    	Gson gson = new Gson(); 
    	String json = gson.toJson(userInfo); 
    	JsonParser parser = new JsonParser();
    	JsonElement element = parser.parse(json);
    	
    	System.out.println("element: "+element);
    	
		String userID = element.getAsJsonObject().get("id").getAsString();
		//디비에서 id 검사
		if(userService.searchUserExist(userID)==0) {
			String userEmail = element.getAsJsonObject().get("email").getAsString();
			String userName = element.getAsJsonObject().get("nickname").getAsString();
			
			User user = new User();
			user.setUserID(userID);
			user.setUserEmail(userEmail);
			user.setUserName(userName);
			userService.insertUser(user);
		}
        return "redirect:http://localhost:3000/?access_Token="+access_Token;
    }
	
}
