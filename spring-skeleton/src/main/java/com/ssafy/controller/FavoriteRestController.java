package com.ssafy.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.model.dto.Favorite;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.FavoriteService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class FavoriteRestController {
	@Autowired
	private FavoriteService favoriteService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("즐겨찾기 추가")
	@PostMapping("/favorite/insert/{yno}_{usno}")
	public ResponseEntity<Map<String, Object>> insertFavorite(@PathVariable int yno, @PathVariable int usno){
		Favorite favorite = new Favorite();
		favorite.setYno(yno);
		favorite.setUsno(usno);
		favoriteService.insertFavorite(favorite); 
		return handleSuccess("즐겨찾기 등록 완료");
	}
	
	@ApiOperation("즐겨찾기 삭제")
	@DeleteMapping("/favorite/delete/{yno}_{usno}")
	public ResponseEntity<Map<String, Object>> searchKeyword(@PathVariable int yno,  @PathVariable int usno){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("usno", usno);
		favoriteService.deleteFavorite(map); 
		return handleSuccess("즐겨찾기 삭제 완료");
	}
	
	@ApiOperation("user 고유번호로 사용자가 즐겨찾기 한 유투버 정보 검색")
	@GetMapping("/favorite/user/{usno}")
	public ResponseEntity<Map<String, Object>> searchUserFavoriteYoutuber(@PathVariable int usno){
		List<Youtuber> list = favoriteService.searchUserFavoriteYoutuber(usno); 
		return handleSuccess(list);
	}
	
	@ApiOperation("유투버 고유번호로 해당 유투버를 즐겨찾기 한 사람 수 조회")
	@GetMapping("/favorite/youtuber/{yno}")
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable int yno){
		int count = favoriteService.searchYoutuberFavoriteNum(yno);
		return handleSuccess(count);
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
