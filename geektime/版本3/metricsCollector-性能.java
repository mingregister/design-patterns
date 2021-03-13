
public class MetricsCollector {
    private static final int DEFAULT_STORAGE_THREAD_POOL_SIZE = 20;
  
    private MetricsStorage metricsStorage;
    private EventBus eventBus;
  
    public MetricsCollector(MetricsStorage metricsStorage) {
      this(metricsStorage, DEFAULT_STORAGE_THREAD_POOL_SIZE);
    }
  
    public MetricsCollector(MetricsStorage metricsStorage, int threadNumToSaveData) {
      this.metricsStorage = metricsStorage;
      this.eventBus = new AsyncEventBus(Executors.newFixedThreadPool(threadNumToSaveData));
      this.eventBus.register(new EventListener());
    }
  
    public void recordRequest(RequestInfo requestInfo) {
      if (requestInfo == null || StringUtils.isBlank(requestInfo.getApiName())) {
        return;
      }
      eventBus.post(requestInfo);
    }
  
    public class EventListener {
      @Subscribe
      public void saveRequestInfo(RequestInfo requestInfo) {
        metricsStorage.saveRequestInfo(requestInfo);
      }
    }
  }