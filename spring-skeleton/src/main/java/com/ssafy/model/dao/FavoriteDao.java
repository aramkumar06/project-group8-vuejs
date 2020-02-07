package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Favorite;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface FavoriteDao {
	public void insertFavorite(Favorite favorite);
	public void deleteFavorite(Map<String, Integer> condition);
	public List<Youtuber> searchUserFavoriteYoutuber(int usno);
	public int searchYoutuberFavoriteNum(int yno);
}
