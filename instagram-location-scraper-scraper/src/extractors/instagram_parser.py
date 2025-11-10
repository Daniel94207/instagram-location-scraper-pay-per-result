thonimport requests
from datetime import datetime

def parse_instagram_location(url, max_items=1000, date_filter=None):
    response = requests.get(url)
    posts = response.json().get('graphql', {}).get('location', {}).get('edge_location_to_media', {}).get('edges', [])
    
    data = []
    for post in posts[:max_items]:
        post_data = {
            'postId': post['node']['id'],
            'code': post['node']['shortcode'],
            'url': f"https://www.instagram.com/p/{post['node']['shortcode']}/",
            'createdAt': datetime.fromtimestamp(post['node']['taken_at_timestamp']).isoformat(),
            'likeCount': post['node']['edge_liked_by']['count'],
            'commentCount': post['node']['edge_media_to_comment']['count'],
            'caption': post['node']['edge_media_to_caption']['edges'][0]['node']['text'] if post['node']['edge_media_to_caption']['edges'] else '',
            'location': post['node'].get('location', {}),
            'owner': post['node']['owner'],
            'video': post['node'].get('video_url', None),
            'image': post['node'].get('display_url', None),
            'audio': post['node'].get('audio_url', None)
        }

        if date_filter:
            post_date = datetime.fromtimestamp(post['node']['taken_at_timestamp'])
            if post_date < date_filter:
                continue

        data.append(post_data)
    
    return data