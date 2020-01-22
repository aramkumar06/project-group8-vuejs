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

import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.YoutuberService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class YoutuberRestController {
	@Autowired
	private YoutuberService youtuberService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("youtuber 고유번호 검색")
	@GetMapping("/youtuber/{yno}")
	public ResponseEntity<Map<String, Object>> search(@PathVariable int yno){
		Youtuber youtuber = youtuberService.search(yno); 
		return handleSuccess(youtuber);
	}
	
	@ApiOperation("youtuber 정보 검색")
	@GetMapping("/youtuber/search/{keyword}")
	public ResponseEntity<Map<String, Object>> searchKeyword(@PathVariable String keyword){
		List<Youtuber> list = youtuberService.searchKeyword(keyword); 
		return handleSuccess(list);
	}
	
	@ApiOperation("전체 youtuber 조회")
	@GetMapping("/youtuber/all")
	public ResponseEntity<Map<String, Object>> searchAll(){
		List<Youtuber> list = youtuberService.searchAll(); 
		return handleSuccess(list);
	}
	
	@ApiOperation("검색 조건에 따른 youtuber 랭킹 조회")
	@GetMapping("/youtuber/rank/{searchCondition}_{num}")
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable String searchCondition, @PathVariable String num){
		Map<String, String> map = new HashMap<>();
		map.put("searchCondition", searchCondition);
		map.put("num", num);
		List<Youtuber> list = youtuberService.searchRanking(map);
		return handleSuccess(list);
	}
	
//	@ApiOperation("youtuber 등록")
//	@PostMapping("/youtuber")
//	public ResponseEntity<Map<String, Object>> insert_youtuber(@RequestBody Youtuber youtuber){
//		youtuberService.insert(youtuber);
//		return handleSuccess("test 등록 완료");
//	}
	
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
