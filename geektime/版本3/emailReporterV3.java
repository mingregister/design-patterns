
public class EmailReporter extends ScheduledReporter {
    // 省略其他代码...
    public void startDailyReport() {
      // new Date()可以获取当前时间
      Date firstTime = trimTimeFieldsToZeroOfNextDay(new Date());
      Timer timer = new Timer();
      timer.schedule(new TimerTask() {
        @Override
        public void run() {
          // 省略其他代码...
        }
      }, firstTime, DAY_HOURS_IN_SECONDS * 1000);
    }
  
    protected Date trimTimeFieldsToZeroOfNextDay(Date date) {
      Calendar calendar = Calendar.getInstance(); // 这里可以获取当前时间
      calendar.setTime(date); // 重新设置时间
      calendar.add(Calendar.DATE, 1);
      calendar.set(Calendar.HOUR_OF_DAY, 0);
      calendar.set(Calendar.MINUTE, 0);
      calendar.set(Calendar.SECOND, 0);
      calendar.set(Calendar.MILLISECOND, 0);
      return calendar.getTime();
    }
  }