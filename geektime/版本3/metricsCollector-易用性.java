
public class MetricsCollector {
    private MetricsStorage metricsStorage;
  
    // 兼顾代码的易用性，新增一个封装了默认依赖的构造函数
    public MetricsCollectorB() {
      this(new RedisMetricsStorage());
    }
  
    // 兼顾灵活性和代码的可测试性，这个构造函数继续保留
    public MetricsCollectorB(MetricsStorage metricsStorage) {
      this.metricsStorage = metricsStorage;
    }
    // 省略其他代码...
  }
  
  public class ConsoleReporter extends ScheduledReporter {
    private ScheduledExecutorService executor;
    
    // 兼顾代码的易用性，新增一个封装了默认依赖的构造函数
    public ConsoleReporter() {
      this(new RedisMetricsStorage(), new Aggregator(), new ConsoleViewer());
    }
  
    // 兼顾灵活性和代码的可测试性，这个构造函数继续保留
    public ConsoleReporter(MetricsStorage metricsStorage, Aggregator aggregator, StatViewer viewer) {
      super(metricsStorage, aggregator, viewer);
      this.executor = Executors.newSingleThreadScheduledExecutor();
    }
    // 省略其他代码...
  }
  
  public class EmailReporter extends ScheduledReporter {
    private static final Long DAY_HOURS_IN_SECONDS = 86400L;
  
    // 兼顾代码的易用性，新增一个封装了默认依赖的构造函数
    public EmailReporter(List<String> emailToAddresses) {
      this(new RedisMetricsStorage(), new Aggregator(), new EmailViewer(emailToAddresses));
    }
    
    // 兼顾灵活性和代码的可测试性，这个构造函数继续保留
    public EmailReporter(MetricsStorage metricsStorage, Aggregator aggregator, StatViewer viewer) {
      super(metricsStorage, aggregator, viewer);
    }
    // 省略其他代码...
  }