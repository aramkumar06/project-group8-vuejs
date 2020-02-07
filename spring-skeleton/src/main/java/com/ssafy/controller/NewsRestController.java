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
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.model.dto.News;
import com.ssafy.model.service.NewsService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class NewsRestController {
	@Autowired
	private NewsService newsService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("news 고유번호 검색")
	@GetMapping("/news/{nno}")
	public ResponseEntity<Map<String, Object>> search(@PathVariable int nno){
		News news = newsService.search(nno); 
		return handleSuccess(news);
	}
	
	@ApiOperation("키워드로 news 정보 검색")
	@GetMapping("/news/search/{keyword}")
	public ResponseEntity<Map<String, Object>> searchKeyword(@PathVariable String keyword){
		List<News> list = newsService.searchKeyword(keyword); 
		return handleSuccess(list);
	}
	
	@ApiOperation("전체 news 조회")
	@GetMapping("/news/all")
	public ResponseEntity<Map<String, Object>> searchAll(){
		List<News> list = newsService.searchAll(); 
		return handleSuccess(list);
	}
	
	@ApiOperation("검색 조건에 따른 news 랭킹 조회")
	@GetMapping("/news/rank/{searchCondition}_{num}")
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable String searchCondition, @PathVariable int num){
		Map<String, String> map = new HashMap<>();
		map.put("searchCondition", searchCondition);
		map.put("num", num + "");
		List<News> list = newsService.searchRanking(map);
		return handleSuccess(list);
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