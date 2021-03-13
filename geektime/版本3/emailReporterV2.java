
public class EmailReporter extends ScheduledReporter {
    // 省略其他代码...
    public void startDailyReport() {
      Date firstTime = trimTimeFieldsToZeroOfNextDay();
      Timer timer = new Timer();
      timer.schedule(new TimerTask() {
        @Override
        public void run() {
          // 省略其他代码...
        }
      }, firstTime, DAY_HOURS_IN_SECONDS * 1000);
    }
  
    // 设置成protected而非private是为了方便写单元测试
    @VisibleForTesting
    protected Date trimTimeFieldsToZeroOfNextDay() {
      Calendar calendar = Calendar.getInstance(); // 这里可以获取当前时间
      calendar.add(Calendar.DATE, 1);
      calendar.set(Calendar.HOUR_OF_DAY, 0);
      calendar.set(Calendar.MINUTE, 0);
      calendar.set(Calendar.SECOND, 0);
      calendar.set(Calendar.MILLISECOND, 0);
      return calendar.getTime();
    }
  }