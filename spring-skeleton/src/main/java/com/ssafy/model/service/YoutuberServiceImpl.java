package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.YoutuberDao;
import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Trend;
import com.ssafy.model.dto.Video;
import com.ssafy.model.dto.Youtuber;

@Service
public class YoutuberServiceImpl implements YoutuberService {

	@Autowired
	private YoutuberDao dao;
	
	@Override
	public Youtuber search(int yno) {
		try {
			return dao.search(yno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 고유번호 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Category> searchCategoryList(int yno) {
		try {
			return dao.searchCategoryList(yno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 고유번호로 카테고리 번호, 카테고리명 검색  중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Youtuber> searchKeyword(String keyword) {
		try {
			return dao.searchKeyword(keyword);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 정보 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Youtuber> searchAll() {
		try {
			return dao.searchAll();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 전체 목록 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Youtuber> searchRanking(Map<String, String> condition) {
		try {
			return dao.searchRanking(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 랭킹 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<News> searchNews(int yno) {
		try {
			return dao.searchNews(yno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 관련 뉴스 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Video> searchVideo(int yno) {
		try {
			return dao.searchVideo(yno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 관련 뉴스 조회 중 에러가 발생했습니다.");
		}
	}

//	@Override
//	public List<Video> searchCommunity(int yno) {
//		try {
//			return dao.searchCommunity(yno);
//		} catch (Exception e) {
//			e.printStackTrace();
//			throw new RuntimeException("youtuber 관련 카테고리 조회 중 에러가 발생했습니다.");
//		}
//	}

	@Override
	public List<Trend> searchTrend(int yno) {
		try {
			return dao.searchTrend(yno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 관련 성장성 데이터 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Video> searchVideoGoodRatio(Map<String, Integer> condition) {
		try {
			return dao.searchVideoGoodRatio(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 상세페이지의 호감도 및 영상 정보 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public double searchGoodRatio(Map<String, Integer> condition) {
		try {
			return dao.searchGoodRatio(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 상세페이지의 호감도 정보 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public int searchVideoCount(Map<String, Integer> condition) {
		try {
			return dao.searchVideoCount(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 상세페이지의 활동지수 정보 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Integer> searchTermVideoCount(Map<String, Integer> condition) {
		try {
			return dao.searchTermVideoCount(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 상세페이지의 기간별 활동지수 정보 조회 중 에러가 발생했습니다.");
		}
	}
}