DB 수정이 발생했을 경우 해당 사항을 models.py에 적용시킬 수 있다.

먼저 `djangoServer` 디렉터리로 bash 실행 위치를 이동하고

아래의 명령어를 입력한다.

```bash
$ python manage.py inspectdb > dataServer/models.py
```

이후 DB의 스키마가 dataServer 앱의 models.py에 옮겨진 것을 확인할 수 있다.

그러나 models.py에서 몇 가지를 수정해야 원활하게 사용할 수 있다.

수정사항은 다음과 같다.

- priamry_key 옵션을 삭제한다.
  - CategoryYoutuberRelation 클래스의 yno의 옵션 중 `primary_key=True`를 삭제한다.
  - Favorite 클래스의 yno 옵션 중 `primary_key=True`를 삭제한다.
- Growth 클래스의 yno에 옵션을 추가한다.
  - `related_name="youtuber_growth"`를 추가한다.


\# 옵션사항

- `on_delete=models.CASCADE`  추가 여부 (현재는 DB 자체 옵션으로 실행 중)

