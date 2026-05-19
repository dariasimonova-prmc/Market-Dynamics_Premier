Generate two outputs based on the source content:

1) Dynamics_Output format, matching the uploaded Excel style:
- 文本 -> 公众号:
  {Mon-DD} | {Brand EN} ({Group EN})\n{Chinese factual detail}

- 文本 -> 微信分享:
  | {MVP_WEEK_CODE}\n\n品牌：{Brand EN} {Brand CN}\n集团：{Group EN} {Group CN}\n时间：{Chinese date}\n地点：{Location}\n参考链接：{Source URL}\n简介：{Chinese factual detail}

2) WeCom internal message format:
【Market Dynamics Update｜市场动态速报】

Brand｜品牌：{Brand EN} {Brand CN}
Source｜来源：{Source Platform}
Activity Type｜动态类型：{Activity Type CN}
Date｜日期：{Published Date}

Core Update｜核心动态：
{Concise factual summary in Chinese}

Strategic Reading｜策略解读：
{One concise business implication. Avoid exaggeration.}

Suggested Follow-up｜建议关注：
{What the team should monitor next}

Source Link｜来源链接：
{URL}

Tone:
- Professional
- Concise
- Suitable for internal luxury market intelligence sharing
- No unsupported claims
- Use Chinese as the main message language unless source is English-only

Return valid JSON only.
