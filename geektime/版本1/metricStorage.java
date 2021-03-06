
public interface MetricsStorage {
  void saveRequestInfo(RequestInfo requestInfo);

  List<RequestInfo> getRequestInfos(String apiName, long startTimeInMillis, long endTimeInMillis);

  Map<String, List<RequestInfo>> getRequestInfos(long startTimeInMillis, long endTimeInMillis);
}

public class RedisMetricsStorage implements MetricsStorage {
  //...省略属性和构造函数等...
  @Override
  public void saveRequestInfo(RequestInfo requestInfo) {
    //...
  }

  @Override
  public List<RequestInfo> getRequestInfos(String apiName, long startTimestamp, long endTimestamp) {
    //...
  }

  @Override
  public Map<String, List<RequestInfo>> getRequestInfos(long startTimestamp, long endTimestamp) {
    //...
  }
}