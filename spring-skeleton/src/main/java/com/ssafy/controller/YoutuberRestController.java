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

import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Trend;
import com.ssafy.model.dto.Video;
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
	
	@ApiOperation("youtuber 고유번호로 카테고리 목록 검색")
	@GetMapping("/youtuber/category/{yno}")
	public ResponseEntity<Map<String, Object>> searchCategoryList(@PathVariable int yno){
		List<Category> list = youtuberService.searchCategoryList(yno); 
		return handleSuccess(list);
	}
	
	@ApiOperation("키워드로 youtuber 정보 검색")
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
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable String searchCondition, @PathVariable int num){
		Map<String, String> map = new HashMap<>();
		map.put("searchCondition", searchCondition);
		map.put("num", num + "");
		List<Youtuber> list = youtuberService.searchRanking(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 관련 뉴스 조회")
	@GetMapping("/youtuber/detail/news/{yno}")
	public ResponseEntity<Map<String, Object>> searchNews(@PathVariable int yno){
		List<News> list = youtuberService.searchNews(yno);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 관련 영상 조회")
	@GetMapping("/youtuber/detail/video/{yno}")
	public ResponseEntity<Map<String, Object>> searchVideo(@PathVariable int yno){
		List<Video> list = youtuberService.searchVideo(yno);
		return handleSuccess(list);
	}
	
//	@ApiOperation("youtuber 관련 커뮤니티 조회")
//	@GetMapping("/youtuber/detail/community/{yno}")
//	public ResponseEntity<Map<String, Object>> searchCommunity(@PathVariable int yno){
//		List<Video> list = youtuberService.searchCommunity(yno);
//		return handleSuccess(list);
//	}
	
	@ApiOperation("youtuber 관련 성장성 데이터 조회")
	@GetMapping("/youtuber/detail/trend/{yno}")
	public ResponseEntity<Map<String, Object>> searchTrend(@PathVariable int yno){
		List<Trend> list = youtuberService.searchTrend(yno);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 상세페이지에 보여줄 가장 최근 동영상 정보 + 좋아요 싫어요 비율 정보(goodRatio) / 최근 영상 num개에 대해서")
	@GetMapping("/youtuber/detail/charm/video/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchVideoGoodRatio(@PathVariable int yno, @PathVariable int num){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		List<Video> list = youtuberService.searchVideoGoodRatio(map);
		return handleSuccess(list);
	}

	@ApiOperation("youtuber 상세페이지에 보여줄 최근 num개 동영상에 대한 좋아요 싫어요 비율 정보(goodRatio) -> 총합산비율 하나만 나옴")
	@GetMapping("/youtuber/detail/charm/goodRatio/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchGoodRatio(@PathVariable int yno, @PathVariable int num){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		double list = youtuberService.searchGoodRatio(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 상세페이지에 보여줄 최근 N달 간 업로드 한 영상 개수")
	@GetMapping("/youtuber/detail/activity/videoCount/{yno}_{term}")
	public ResponseEntity<Map<String, Object>> searchVideoCount(@PathVariable int yno, @PathVariable int term){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("term", term);
		int list = youtuberService.searchVideoCount(map);
		return handleSuccess(list);
	}

	@ApiOperation("유투버 상세페이지에 보여줄 num주(or 달)간 영상 개수  / 과거 등록일부터 ")
	@GetMapping("/youtuber/detail/activity/termVideoCount/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchTermVideoCount(@PathVariable int yno, @PathVariable int num){
		
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		
//		List<Integer> list = new LinkedList<>();
//		for (int i = 1; i <= end; i++) {
//			map.put("yno", yno + "");
//			map.put("start", -1 * (i - 1) + "");
//			map.put("end", -1 * i + "");
//			list.add(i + "주 전", youtuberService.searchTermVideoCount(map));
//			map.clear();
//		}
		List<Integer> list = youtuberService.searchTermVideoCount(map);
		return handleSuccess(list);
	}
	
//	@ApiOperation("youtuber 상세페이지의 호감도 정보 조회")
//	@GetMapping("/youtuber/detail/activity/termVideoCount/{yno}_{start}_{end}_{term}")
//	public ResponseEntity<Map<String, Object>> searchTermVideoCount(@PathVariable int yno, @PathVariable int start, @PathVariable int end, @PathVariable String term){
//		Map<String, String> map = new HashMap<>();
//		map.put("yno", yno + "");
//		map.put("start", start + "");
//		map.put("end", end + "");
//		map.put("term", term);
//		int list = youtuberService.searchTermVideoCount(map);
//		return handleSuccess(list);
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