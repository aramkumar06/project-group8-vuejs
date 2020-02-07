package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Favorite;
import com.ssafy.model.dto.Youtuber;

public interface FavoriteService {
	public void insertFavorite(Favorite favorite);
	public void deleteFavorite(Map<String, Integer> condition);
	public List<Youtuber> searchUserFavoriteYoutuber(int usno);
	public int searchYoutuberFavoriteNum(int yno);
}