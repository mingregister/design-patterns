
public class ConsoleReporter {
    private MetricsStorage metricsStorage;
    private ScheduledExecutorService executor;
  
    public ConsoleReporter(MetricsStorage metricsStorage) {
      this.metricsStorage = metricsStorage;
      this.executor = Executors.newSingleThreadScheduledExecutor();
    }
    
    // 第4个代码逻辑：定时触发第1、2、3代码逻辑的执行；
    public void startRepeatedReport(long periodInSeconds, long durationInSeconds) {
      executor.scheduleAtFixedRate(new Runnable() {
        @Override
        public void run() {
          // 第1个代码逻辑：根据给定的时间区间，从数据库中拉取数据；
          long durationInMillis = durationInSeconds * 1000;
          long endTimeInMillis = System.currentTimeMillis();
          long startTimeInMillis = endTimeInMillis - durationInMillis;
          Map<String, List<RequestInfo>> requestInfos =
                  metricsStorage.getRequestInfos(startTimeInMillis, endTimeInMillis);
          Map<String, RequestStat> stats = new HashMap<>();
          for (Map.Entry<String, List<RequestInfo>> entry : requestInfos.entrySet()) {
            String apiName = entry.getKey();
            List<RequestInfo> requestInfosPerApi = entry.getValue();
            // 第2个代码逻辑：根据原始数据，计算得到统计数据；
            RequestStat requestStat = Aggregator.aggregate(requestInfosPerApi, durationInMillis);
            stats.put(apiName, requestStat);
          }
          // 第3个代码逻辑：将统计数据显示到终端（命令行或邮件）；
          System.out.println("Time Span: [" + startTimeInMillis + ", " + endTimeInMillis + "]");
          Gson gson = new Gson();
          System.out.println(gson.toJson(stats));
        }
      }, 0, periodInSeconds, TimeUnit.SECONDS);
    }
  }
  
  public class EmailReporter {
    private static final Long DAY_HOURS_IN_SECONDS = 86400L;
  
    private MetricsStorage metricsStorage;
    private EmailSender emailSender;
    private List<String> toAddresses = new ArrayList<>();
  
    public EmailReporter(MetricsStorage metricsStorage) {
      this(metricsStorage, new EmailSender(/*省略参数*/));
    }
  
    public EmailReporter(MetricsStorage metricsStorage, EmailSender emailSender) {
      this.metricsStorage = metricsStorage;
      this.emailSender = emailSender;
    }
  
    public void addToAddress(String address) {
      toAddresses.add(address);
    }
  
    public void startDailyReport() {
      Calendar calendar = Calendar.getInstance();
      calendar.add(Calendar.DATE, 1);
      calendar.set(Calendar.HOUR_OF_DAY, 0);
      calendar.set(Calendar.MINUTE, 0);
      calendar.set(Calendar.SECOND, 0);
      calendar.set(Calendar.MILLISECOND, 0);
      Date firstTime = calendar.getTime();
      Timer timer = new Timer();
      timer.schedule(new TimerTask() {
        @Override
        public void run() {
          long durationInMillis = DAY_HOURS_IN_SECONDS * 1000;
          long endTimeInMillis = System.currentTimeMillis();
          long startTimeInMillis = endTimeInMillis - durationInMillis;
          Map<String, List<RequestInfo>> requestInfos =
                  metricsStorage.getRequestInfos(startTimeInMillis, endTimeInMillis);
          Map<String, RequestStat> stats = new HashMap<>();
          for (Map.Entry<String, List<RequestInfo>> entry : requestInfos.entrySet()) {
            String apiName = entry.getKey();
            List<RequestInfo> requestInfosPerApi = entry.getValue();
            RequestStat requestStat = Aggregator.aggregate(requestInfosPerApi, durationInMillis);
            stats.put(apiName, requestStat);
          }
          // TODO: 格式化为html格式，并且发送邮件
        }
      }, firstTime, DAY_HOURS_IN_SECONDS * 1000);
    }
  }